# Copyright (c) 2009 The Foundry Visionmongers Ltd.  All Rights Reserved.

## init.py
## loaded by nuke before menu.py
import sys
import nuke
from scripts import slate
from scripts import ftrackUpload
from scripts import writeNodeManager
from scripts import readNodeManager

print "Loading init.py...."
nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./icons')
