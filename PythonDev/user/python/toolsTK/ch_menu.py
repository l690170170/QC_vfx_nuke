import toolsTK.common as tk
import os



if os.getenv('CH_ROOT_MENU'):
    rootMenu=os.getenv('CH_ROOT_MENU')
else:
    rootMenu='toolsTK'
    
menubar=nuke.menu("Nuke")

m=menubar.findItem(rootMenu)
if m:
    m.clearMenu()
    print 'Menu refreshed...'
else:
    m=menubar.addMenu(rootMenu)

# Path to the toolssets uncomment proper line depending on your OS (Win/lin)
# toolsetpath='/sft/tools/Nuke/Toolsets'
toolsetpath='%s/Toolsets' % os.path.dirname(__file__)

# 3D
m.addCommand("3d/fakeVolume", "nuke.loadToolset('%s/3d/fakeVolume.nk')"% toolsetpath)


m.addCommand("Sys/Update menu", "nuke.load('ch_menu.py')")




import toolsTK.common as tk


print 'chMenu loaded'

if os.getenv('CH_ROOT_MENU'):
    rootMenu=os.getenv('CH_ROOT_MENU')
else:
    rootMenu='toolsTK'
    
menubar=nuke.menu("Nuke")

m=menubar.findItem(rootMenu)
if m:
    m.clearMenu()
    print 'Menu refreshed...'
else:
    m=menubar.addMenu(rootMenu)


# AUTO BACKDROP OVERRIDE

import toolsTK.autoBackdrop as autoBackdrop
nukescripts.autoBackdrop = autoBackdrop.autoBackdrop

m.addCommand("Utilities/Backdrop", 'nukescripts.autoBackdrop()','#b')


m.addCommand("Sys/Update menu", "nuke.load('ch_menu.py')")



#m.addCommand("AutoRead", "nuke.load('ch_autoRead.py'),ch_createCompTemplate()")
#m.addCommand("FULLAUTO", "nuke.load('ch_autoRead.py'),ch_fullAuto()")

""" adv IP Menu """
#import toolsTK.chViewerInput as tkViewerInput
#tkViewerInput.menuInit()

