import ftrack_api
import os
import threading
import nuke
import json
import writeNodeManager
import shutil
from Utils import ftrack_utils2


_session = ftrack_api.Session(
    server_url=os.environ['FTRACK_SERVER'],
    api_user=os.environ['FTRACK_API_USER'],
    api_key=os.environ['FTRACK_API_KEY']
)


def async(fn):
    """Run *fn* asynchronously."""
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
    return wrapper


def prepMediaFiles(outputFile):
    outfilemp4 = os.path.splitext(outputFile)[0] + '.mp4'
    outfilewebm = os.path.splitext(outputFile)[0] + '.webm'
    thumbnail = os.path.splitext(outputFile)[0] + '_thumbnail.png'
    metadata = {
        'source_file': outputFile
        }
    return outfilemp4, outfilewebm, thumbnail, metadata


def deleteFiles(outfilemp4, outfilewebm, thumbnail):
    if os.path.exists(outfilemp4):
        os.remove(outfilemp4)
    if os.path.exists(outfilewebm):
        os.remove(outfilewebm)
    if os.path.exists(thumbnail):
        os.remove(thumbnail)


def createRVComponent(session, version, outputFile):
    server_location = session.query('Location where name is "ftrack.unmanaged"').one()
    component = version.create_component(
        path=outputFile,
        data={
            'name': 'movie'
        },
        location=server_location
    )
    component.session.commit()


def getOutputFile():
    rootDir = writeNodeManager.getRootDir()
    filename = writeNodeManager.getFilename()
    outputFile = '%simg/comps/%s.mov' % (rootDir, filename)
    return outputFile


def copyToApprovals(outputFile):
    filename = os.path.split(outputFile)[-1]
    projFolder = outputFile.split('shots')[0]
    approvals = os.path.join(projFolder, 'production', 'approvals')
    date = getDate()
    appFolder = os.path.join(approvals, date)
    if not os.path.exists(appFolder):
        os.makedirs(appFolder)
    os.chmod(appFolder, 0777)
    dstFile = os.path.join(appFolder, filename)
    shutil.copyfile(outputFile, dstFile)
    return dstFile


def getDate():
    import datetime
    today = datetime.datetime.today()
    if today.hour > 10:
        dailiesDate = today + datetime.timedelta(1)
    else:
        dailiesDate = today
    date = '%d-%02d-%02d' % (dailiesDate.year, dailiesDate.month, dailiesDate.day)
    return date


@async
def uploadToFtrack():
    node = None
    nukeFile = nuke.scriptName()

    for write in nuke.allNodes('Write'):
        if write.name() == 'Write_mov':
            node = write
            break

    if node and node.knob('uploadToFtrack').value() and not \
            nukeFile.endswith('.autosave'):
        print "Submitting to Dailies"

        outputFile = writeNodeManager.getOutputFile()
        if 'FTRACK_TASKID' in os.environ:
            taskid = os.environ['FTRACK_TASKID']
        else:
            taskid = None
        task = ftrack_utils2.getTask(_session, taskid, nukeFile)
        node.knob('uploadToFtrack').setValue(False)
        if task:
            taskMeta = {'filename': nukeFile}
            fps = int(task['project']['custom_attributes']['fps'])
            ftrack_utils2.addMetadata(_session, task, taskMeta)
            ftrack_utils2.copyToApprovals(outputFile, task['project'])
            outfilemp4, outfilewebm, thumbnail, metadata = ftrack_utils2.prepMediaFiles(outputFile)
            print "Starting conversion..."
            result = ftrack_utils2.convertFiles(outputFile, outfilemp4, outfilewebm, thumbnail)
            if result:
                print "File conversion complete. Starting upload."
                asset = ftrack_utils2.getAsset(_session, task, 'ReviewAsset')
                status = ftrack_utils2.getStatus(_session, 'Pending Internal Review')
                ff = int(nuke.tcl('frames first'))
                lf = int(nuke.tcl('frames last'))
                try:
                    ftrack_utils2.createAndPublishVersion(_session, task, asset,
                                                          status,'Upload for Internal Review',
                                                          thumbnail, outputFile, outfilemp4,
                                                          outfilewebm, metadata, ff, lf, fps)
                    print 'cleaning up temporary files...'
                    ftrack_utils2.deleteFiles(outfilemp4, outfilewebm, thumbnail)
                    print 'Upload Complete!'
                except Exception:
                    print "Error while uploading movie"
                ftrack_utils2.syncToJHB(outputFile)
        else:
            nuke.message("Error in submitting to ftrack. The project details might be incorrect.")
