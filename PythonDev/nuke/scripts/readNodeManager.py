import nuke
import os
import json


def findOutFile(plateDir, fext):
    outfile = ''
    for f in os.listdir(plateDir):
        if os.path.isfile(os.path.join(plateDir,f)):
            if os.path.splitext(f)[1] == fext:
                tmp = f.split(fext)[0]
                tmpSplit = tmp.split('.')[-1]
                if tmpSplit.isdigit(): # if filename ends with frame number, then remove frame no.
                    tmp = tmp.strip(tmpSplit)
                    padding = len(tmpSplit)
                    outfile = '{0}{1:#<{2}}{3}'.format(tmp, '', padding, fext)
                    break
    return outfile

def findMovieFile(plateDir):
    outfile = ''
    for f in os.listdir(plateDir):
        if os.path.isfile(os.path.join(plateDir,f)):
            if os.path.splitext(f)[1] == '.mov':
                outfile = f
                break
    return outfile


def getProxyPath():
    outfile = outfilePath = ''
    filename = nuke.scriptName()
    shotDir = filename.split('scene')[0]
    plateDir = os.path.join(shotDir, 'img/plates/')
    proxyDir = os.path.join(shotDir, 'img/plates/proxy')
    if os.path.exists(proxyDir):
        outfile = findOutFile(proxyDir, '.jpeg')
        #Try and find a movie if no jpeg found
        if outfile == '':
            outfile = findMovieFile(plateDir)
            if outfile is not '':
                outfilePath = os.path.join(plateDir, outfile)
        else:
            outfilePath = os.path.join(proxyDir, outfile)
    return outfilePath


def getReadPath():
    filename = nuke.scriptName()
    shotDir = filename.split('scene')[0]
    plateDir = os.path.join(shotDir, 'img/plates/')
    #Try and find a dpx
    outfile = findOutFile(plateDir, '.dpx')
    outfilePath = ''
    if outfile == '':
        #Try and find a jpeg if no dpx found
        proxyDir = os.path.join(shotDir, 'img/plates/proxy')
        if os.path.exists(proxyDir):
            outfile = findOutFile(proxyDir, '.jpeg')
        #Try and find a movie if no jpeg found
        if outfile == '':
            outfile = findMovieFile(plateDir)
            if outfile is not '':
                outfilePath = os.path.join(plateDir, outfile)
        else:
            outfilePath = os.path.join(proxyDir, outfile)
    else:
        outfilePath = os.path.join(plateDir, outfile)

    return outfilePath


def findFrameByExt(plateDir, fext):
    frameList = []
    for f in os.listdir(plateDir):
        if os.path.isfile(os.path.join(plateDir,f)) and os.path.splitext(f)[1] == fext:
            tmp = f.split(fext)[0]
            tmpSplit = tmp.split('.')[-1]
            if tmpSplit.isdigit():
                frameList.append(int(tmpSplit))
    return frameList


def getFramesProxy(position):
    filename = nuke.scriptName()
    shotDir = filename.split('scene')[0]
    proxyDir = os.path.join(shotDir, 'img/plates/proxy')
    frameList = []
    if os.path.exists(proxyDir):
        frameList = findFrameByExt(proxyDir, '.jpeg')
    if len(frameList) > 0:
        frameList.sort()
        if position == 'first':
            return frameList[0]
        elif position == 'last':
            return frameList[-1]
    else:
        return 1


def getFrames(position):
    filename = nuke.scriptName()
    shotDir = filename.split('scene')[0]
    plateDir = os.path.join(shotDir, 'img/plates')
    frameList = findFrameByExt(plateDir, '.dpx')
    if len(frameList) == 0:
        proxyDir = os.path.join(shotDir, 'img/plates/proxy')
        if os.path.exists(proxyDir):
            frameList = findFrameByExt(proxyDir, '.jpeg')
    if len(frameList) > 0:
        frameList.sort()
        if position == 'first':
            return frameList[0]
        elif position == 'last':
            return frameList[-1]
    else:
        return 1


def getJsonFilePath():
    filename = nuke.scriptName()
    tmpDir = os.path.split(filename)[0]
    jsonFile = os.path.join(tmpDir, 'shot_info.json')
    if not os.path.exists(jsonFile):
        return ''
    jd = open(jsonFile).read()
    data = json.loads(jd)
    fext = data['outfile'].split('.')[-1]
    outFile = findOutFile(data['outdir'], '.'+fext)
    outFilePath = os.path.join(data['outdir'], outFile)
    return outFilePath


def getJsonFrames(position):
    filename = nuke.scriptName()
    tmpDir = os.path.split(filename)[0]
    jsonFile = os.path.join(tmpDir, 'shot_info.json')
    if not os.path.exists(jsonFile):
        return 1
    jd = open(jsonFile).read()
    data = json.loads(jd)
    fext = data['outfile'].split('.')[-1]
    frameList = findFrameByExt(data['outdir'], '.'+fext)
    if len(frameList) > 0:
        frameList.sort()
        if position == 'first':
            return frameList[0]
        elif position == 'last':
            return frameList[-1]
    else:
        return 1
