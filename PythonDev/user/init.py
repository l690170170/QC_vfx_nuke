# Copyright (c) 2014 The Foundry Visionmongers Ltd.  All Rights Reserved.
 
## init.py
## loaded by nuke before menu.py
 
nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./icons')



#add a network location for gizmos and stuff
#nuke.pluginAddPath('Z://1_jobs//_JobTools//scripts//nuke_gizmos')

#import platform
#def filenameFix(filename):
#if platform.system() in ("Windows", "Microsoft"):
#return filename.replace( "/SharedDisk/", "p:\" )
#else:
#return filename.replace( "p:\", "/SharedDisk/" )
#return filename


#import platform
#def filenameFix(filename):
#if platform.system() in ("Windows", "Microsoft"):
#return filename.replace( "//nukescripts", "//My Documents//nukescripts//" )
#else:
#return filename.replace( "//My Documents//nukescripts", "//nukescripts//" )
#return filename

#windows environment

#if sys.platform == 'darwin':

#nuke.pluginAddPath(os.path.expanduser("~//My Documents//nukescripts"))
#nuke.pluginAddPath(os.path.expanduser("~//My Documents//nukescripts//plugins"))
#nuke.pluginAddPath(os.path.expanduser("~//My Documents//nukescripts//python"))
#nuke.pluginAddPath(os.path.expanduser("~//My Documents//nukescripts//tcl"))
#nuke.pluginAddPath(os.path.expanduser("~//My Documents//nukescripts//gizmos"))
#nuke.pluginAddPath(os.path.expanduser("~//My Documents//nukescripts//icons"))

#linux environment
nuke.pluginAddPath(os.path.expanduser("~//nukescripts"))
nuke.pluginAddPath(os.path.expanduser("~//nukescripts//plugins"))
nuke.pluginAddPath(os.path.expanduser("~//nukescripts//python"))
nuke.pluginAddPath(os.path.expanduser("~//nukescripts//tcl"))
nuke.pluginAddPath(os.path.expanduser("~//nukescripts//gizmos"))
nuke.pluginAddPath(os.path.expanduser("~//nukescripts//icons"))

nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./python')
nuke.pluginAddPath('./icons')




###adding pluginpaths for Tools###

"""path to all the menu-icons"""
nuke.pluginAddPath('./Icons')


"""path to tools folder, (where the python scripts is located)"""
nuke.pluginAddPath('./Tools')

nuke.pluginAddPath( './_gizmos' )


nuke.pluginAddPath('./python')
nuke.pluginAddPath('./python/toolsTK')


import reformat_presets
reformat_presets.nodePresetReformat()

import cam_presets
cam_presets.nodePresetCamera()


import rollingshutter_presets
rollingshutter_presets.nodePresetRollingShutter()






nuke.pluginAddPath('./python')
nuke.pluginAddPath('./python/toolsTK')

import toolsTK.common as tk


nuke.pluginAddPath('V:\SendNodes_v1.2')


import nuke

nuke.pluginAddPath('pixelfudger')





import nuke
nuke.pluginAddPath("SCRIPT")



nuke.pluginAddPath("fileCollector")