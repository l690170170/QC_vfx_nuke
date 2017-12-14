import nuke
import os

selectedNodes = nuke.selectedNodes()
for readNode in selectedNodes:
    path=readNode.knob('file').value()
    path=path.replace(path.split("/")[-1],"")
    os.system('explorer %s'%path.replace("/","\\"))