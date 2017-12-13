import nuke
import nukescripts
import os
import re


def save():
    filename = nuke.scriptName()
    nkDir, nkFile = os.path.split(filename)
    name, ext = os.path.splitext(nkFile)

    fileSaved = False
    components = name.split('_v')
    shotName = components[0]
    if len(components)<=1:
        version = 0
    else:
        version = int(components[1])
    while not fileSaved:
        # CONSTRUCT FILE NAME
        nkName = '%s_v%02d' % ( shotName, version )
        # JOIN DIRECTORY AND NAME TO FORM FULL FILE PATH
        nkPath = os.path.join( nkDir, '%s.nk' % nkName )
        if os.path.isfile(nkPath):
            version += 1
            continue
        updateWriteNodeVersions(version)
        # SAVE NUKE SCRIPT
        nuke.scriptSaveAs(nkPath)
        fileSaved = True
    return nkPath


def updateWriteNodeVersions(version):
    pattern = re.compile(r'v\d\d')
    writeNodes = nuke.allNodes('Write')
    for writeNode in writeNodes:
        filename = writeNode.knob('file').value()
        searchStr = pattern.search(filename)
        if searchStr:
            oldVersion = searchStr.group()
            filename = filename.replace(oldVersion, 'v%02d' % version)
            writeNode.knob('file').setValue(filename)
