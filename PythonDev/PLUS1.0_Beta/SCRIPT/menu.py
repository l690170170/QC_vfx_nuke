import nuke, nukescripts, sys, os, errno

from AddPlus import *
from Directories import *
from Relative import *
from Organize import *
from LockPanel import *
from Multiple import *
from CP_to_Matrix import *
from ThreeD import *
from TwoD import *
from CP_to_Matrix import *
from curveGenBake import *


toolbar = nuke.toolbar ( "PLUS" )
Dir = toolbar.addMenu ( 'Directories', icon = 'admin.png' )
Dir.addCommand( 'Add Plus Control', "addPlus()" , icon='Dplus.png')
Dir.addSeparator()
Dir.addCommand( 'Open tmp Folder', "opentmp()", 'shift+t' , icon='Dtmp.png')
Dir.addCommand( 'Open Script Folder', "openScriptFolder()" ,'shift+j' , icon='Dscript.png')
Dir.addCommand( 'Open Project Folder', "openProjectFolder()", icon='Dproject.png')
Dir.addCommand( 'Open selected Nodes', "plusOpen_toolbar()", icon='Dnodes.png')
Dir.addSeparator()
Dir.addCommand( 'Make Selected Relative', "make_relative_Toolbar()", icon='TDreltv.png')
Dir.addCommand( 'Make Selected absolute', "make_obsolute_Toolbar()", icon='TDabsolute.png')
Dir.addSeparator()
Dir.addCommand( 'Read from Write', "PlusRFWLink_toolbar()",'shift+e' ,  icon='Drfw.png')
Dir.addCommand( 'Create Proxy', "CreatePRX_toolbar()", icon='Dproxy.png')

TwoD = toolbar.addMenu ( '2D Menu', icon = 'TWOD.png' )
TwoD.addCommand( 'AA', 'nuke.createNode("AA")' , icon='TDaa.png' )
TwoD.addCommand( 'Fix NaN', 'nuke.createNode("PlusNaN")', icon='TDnan.png' )
TwoD.addCommand( 'Curve Generator', 'nuke.createNode("CurveGen")', icon='TDcg.png'  )
TwoD.addCommand( 'Active Crop ', "PlusCrop()" , icon='TDcrop.png' )
TwoD.addSeparator()
TwoD.addCommand( 'CornerPin to Matrix', "CP_to_Matrix_toolbar()",  icon='TDcptm.png')
TwoD.addCommand( 'Matrix to CornerPin', "Matrix_to_CP_toolbar()",  icon='TDmtcp.png')

Multiple = toolbar.addMenu ( 'Multiple', icon = 'Multiple.png' )
Multiple.addCommand( 'Reload all reads', "reloadReads()", icon='Mrel.png')
Multiple.addCommand( 'Multiple Reads', "showMulReads()", icon='Mread.png')
Multiple.addCommand( 'Multiple Nodes', "showMulNodes()", icon='Mnodes.png')

ThreeD = toolbar.addMenu ( '3D Menu', icon = 'THREED.png' )
ThreeD.addCommand( 'Track To 3D', "nuke.createNode('TrackTo3D')",  icon='THDtrck.png')
ThreeD.addCommand( 'Stereo from Cam', "stereoRig_toolbar()", icon='THDstereo.png' )
ThreeD.addCommand( 'Bake Under Parent', "BakeUnderParent()",  icon='THDbake.png')

Organize = toolbar.addMenu ( 'Organize', icon = 'Orga.png' )
Organize.addCommand( 'Node Class', 'whatClass()', icon = 'Oc.png')
Organize.addCommand( 'RGB To Hex', "rgbToHex()", icon = 'Ohex.png' )
Organize.addSeparator()
Organize.addCommand( 'Change Color', "NodesColor()", icon = 'Ocolor.png' )
Organize.addCommand( 'Add Label', 'AddLabel()' , icon = 'Olabel.png')
Organize.addCommand( 'Remove Label', 'RemoveLabel()', icon = 'Orlabel.png' )
Organize.addSeparator()
Organize.addCommand( 'add icons', "addIcons()", icon = 'Oi.png' )
Organize.addCommand( 'remove icons', "removeIcons()",  icon = 'Ori.png')
Organize.addCommand( 'copy icons', "copyIcons()",  icon = 'Oci.png')
Organize.addSeparator()
Organize.addCommand( 'Lock Panel', 'showLockPanel()' ,'shift+i' , icon = 'Olp.png')
Organize.addCommand( 'lock selected node', "LockNodes()",  icon = 'Oln.png')
Organize.addCommand( 'unlock selected node', "UnlockNodes()",  icon = 'Oun.png')
Organize.addCommand( 'Hide selected node', "HideNodes()",  icon = 'Ohn.png')
Organize.addCommand( 'unhide selected node', "UnhideNodes()",   icon = 'Ouhn.png')

