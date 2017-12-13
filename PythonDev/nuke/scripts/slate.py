import ftrack_api
import os
import json
import threading
import nuke
import time
import writeNodeManager
import shutil
import datetime
from Utils import ftrack_utils2


_session = ftrack_api.Session(
        server_url=os.environ['FTRACK_SERVER'],
        api_user=os.environ['FTRACK_API_USER'],
        api_key=os.environ['FTRACK_API_KEY']
    )



def getTask():
    nukeFile = nuke.scriptName()

    if 'FTRACK_TASKID' in os.environ:
        taskid = os.environ['FTRACK_TASKID']
    else:
        taskid = None
    task = ftrack_utils2.getTask(_session, taskid, nukeFile)
    return task


def getArtist():
    username = ''
    task = getTask()
    if task:
        try:
            username = task['appointments'][0]['resource']['username']
        except:
            username = 'No user assigned'
    return username


def getLatestNote():
    latestNote = ''
    task = getTask()
    if task:
        notesDict = {}
        for note in task['notes']:
            notesDict[note['date']] = note['content']

        if len(task['notes']) > 0:
            latestDate = sorted(notesDict.keys())[-1]
            latestNote = notesDict[latestDate]
    return latestNote


def getLineDict():
    note = getLatestNote()
    lines = {}
    if note is not '':
        parts = note.split('\n')
        i = 1
        for part in parts:
            if not part == '':
                if i <= 4:
                    lines[i] = part
                    i += 1
                else:
                    lines[4] = lines[4] + ' ' + part
    return lines


def getLine(lineno):
    lines = getLineDict()
    line = ''
    if lineno in lines:
        line = lines[lineno]
    #return line
    return '' # Removing notes feature


def getDate():
    today = datetime.datetime.today()
    date = '%d-%02d-%d' % (today.year, today.month, today.day)
    return date


def getVersion():
    nukeFile = nuke.scriptName()
    try:
        version = int(ftrack_utils2.version_get(nukeFile, 'v')[1])
    except ValueError:
        version = 0
    return version


def getShotName():
    shotName = ''
    task = getTask()
    if task:
        shotName = task['parent']['name']
    return shotName


def getJobName():
    jobName = ''
    task = getTask()
    if task:
        jobName = task['project']['name']
    return jobName


def getTaskName():
    taskName = ''
    task = getTask()
    if task:
        taskName = task['name']
    return taskName


def readJson():
    filename = nuke.scriptName()
    tmpDir = os.path.split(filename)[0]
    jsonFile = os.path.join(tmpDir, 'shot_info.json')
    if not os.path.exists(jsonFile):
        return None
    jd = open(jsonFile).read()
    data = json.loads(jd)
    return data


def getShotNameFromJson():
    data = readJson()
    if not data:
        return ''
    return data['shotName']


def getJobNameFromJson():
    data = readJson()
    if not data:
        return ''
    return data['projectName']


def getVersionFromJson():
    data = readJson()
    if not data:
        return ''
    return data['version']


def getArtistFromJson():
    data = readJson()
    if not data:
        return ''
    return data['username']


def getTaskFromJson():
    data = readJson()
    if not data:
        return ''
    return data['taskName']
