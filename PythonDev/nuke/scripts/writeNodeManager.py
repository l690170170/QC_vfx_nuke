import nukescripts
import json
import nuke
import os
from datetime import datetime


def getRootDir():
    nukeFile = nuke.scriptName()
    return nukeFile.split('compscript')[0]


def getFilename():
    nukeFile = nuke.root().name()
    return nukeFile.split('/')[-1].split('.')[0]


def getFilenameMatte():
    filename = getFilename()
    return filename.replace('comp', 'matte')


def getOutputFile():
    node = nuke.thisNode()
    outfile = node.knob('file').value()
    if 'writeNodeManager.setOutputPath' in outfile:
        type = outfile.split("writeNodeManager.setOutputPath('")[-1].split("')")[0]
        outfile = setOutputPath(type)
    elif 'writeNodeManager.setJsonOutputPath' in outfile:
        outfile = setJsonOutputPath()
    return outfile


def getDate():
    today = datetime.today()
    date = '%d_%02d_%02d' % (today.year, today.month, today.day)
    return date


def getShotName():
    nukeFile = nuke.root().name()
    shotname = nukeFile.split('/')[4]
    return shotname


def getProjectName():
    nukeFile = nuke.root().name()
    projname = nukeFile.split('/')[1]
    if projname == 'bg_tlf':
        projname = 'TLF'
    return projname


def getProjectDir():
    nukeFile = nuke.root().name()
    parts = nukeFile.split('/')
    projDir = os.path.join(parts[0], '/%s' % parts[1])
    return projDir


def getVersion():
    filename = getFilename()
    version = filename.split('_')[-1]
    return int(version.split('v')[-1])


def makeFolders(folder):
    folder = folder.replace('/', '\\')
    if not os.path.exists(folder):
        os.makedirs(folder)


def getFinalQuickTimeFolder():
    rootDir = '%s/production/deliveries/locovfx_%s_a' % (getProjectDir(), getDate())
    filename = getFilename()
    qtFolder = '%s/_quicktime/comp/%s' % (rootDir, filename)
    makeFolders(qtFolder)
    return qtFolder


def getQuickTimeFolder():
    rootDir = '%s/production/approvals/bg/locovfx_%s_a' % (getProjectDir(), getDate())
    filename = getFilename()
    qtFolder = '%s/_quicktime/comp/%s' % (rootDir, filename)
    makeFolders(qtFolder)
    return qtFolder


def getDPXRoot():
    rootDir = '%s/production/deliveries/locovfx_%s_a' % (getProjectDir(), getDate())
    dpxRoot = '%s/_dpx/' % rootDir
    return dpxRoot


def getDPXComp():
    dpxRoot = getDPXRoot()
    filename = getFilename()
    dpxComp = '%s/comp/%s' % (dpxRoot, filename)
    makeFolders(dpxComp)
    return dpxComp


def getDPXMatte():
    dpxRoot = getDPXRoot()
    filename = getFilenameMatte()
    dpxMatte = '%s/matte/%s' % (dpxRoot, filename)
    makeFolders(dpxMatte)
    return dpxMatte


def copyNukeFile():
    rootDir = '%s/production/deliveries/locovfx_%s_a' % (getProjectDir(), getDate())
    shotname = getShotName()
    filename = getFilename()
    nkFolder = '%s/_nk/%s/compscript/%s' % (rootDir, shotname, filename)
    makeFolders(nkFolder)
    nukeFile = nuke.root().name()
    import shutil
    shutil.copy(nukeFile, nkFolder)


def setOutputPath(type):
    filename = nuke.scriptName()
    filepath, file = os.path.split(filename)
    fname, fext = os.path.splitext(file)
    version = fname.split('_')[-1]
    shotDir = filename.split('scene')[0]
    parentDir = os.path.dirname(filename)
    if os.path.split(parentDir)[-1] == 'rotoscoping':
        compDir = os.path.join(shotDir, 'img/roto/%s' % version)
    else:
        compDir = os.path.join(shotDir, 'img/comps/%s' % version)
    outDir = os.path.join(compDir, type)
    if not os.path.exists(outDir):
        os.makedirs(outDir)
    thisNode = nuke.thisNode()
    fileType = thisNode.knob('file_type').value()
    if type == 'img':
        outFile = os.path.join(outDir, '%s.####.%s' % (fname, fileType))
    elif type == 'mov':
        outFile = os.path.join(outDir, '%s.%s' % (fname, fileType))
    elif type == 'qc':
        outFile = os.path.join(outDir, '%s_qc.%s' % (fname, fileType))
    return outFile


def checkDailiesTab():
    # onScriptLoad callback. Checks if Dailies tab exists.
    # If not, adds it to Write_mov node
    node = nuke.toNode('Write_mov')
    if node and not 'Dailies' in node.knobs():
        userTab = nuke.Tab_Knob('Dailies')
        node.addKnob(userTab)
        sc = nuke.PyScript_Knob('submit', 'Submit To Dailies',
                                "node = nuke.thisNode()\nnode.knob('uploadToFtrack').setValue(True)\nnukescripts.render_panel((node,), False)")
        node.addKnob(sc)
        chk = nuke.Boolean_Knob('uploadToFtrack', 'uploadToFtrack')
        node.addKnob(chk)
        chk.setVisible(False)


def setJsonOutputPath():
    filename = nuke.scriptName()
    tmpDir = os.path.split(filename)[0]
    jsonFile = os.path.join(tmpDir, 'shot_info.json')
    if not os.path.exists(jsonFile):
        return ''
    jd = open(jsonFile).read()
    data = json.loads(jd)
    outFilename = data['outfile'].split('.')[0]
    outputFile = os.path.join(data['outdir'], outFilename + '.mov')
    return outputFile
