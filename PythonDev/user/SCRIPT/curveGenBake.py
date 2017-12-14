import nuke
import os

def curveGenBakeAxis():

    This = nuke.thisNode()
    xps = This['xpos'].value()
    yps = This['ypos'].value()
    nuke.root().begin()
    target = nuke.nodes.Axis2(name=This.name()+'_3DBaked', xpos=xps+100, ypos = yps)

    targetknob = target['translate']
    targetknob.setAnimated()
    
    
    #BAKING ANIMATION
    x = nuke.root().firstFrame()
    while x <= nuke.root().lastFrame():
        valuex = This['CURVE'].valueAt(x)[0]
        valuey = This['CURVE'].valueAt(x)[1]
        valuez = This['CURVE'].valueAt(x)[2]
        targetknob.setValueAt(valuex, x, 0)
        targetknob.setValueAt(valuey, x, 1)
        targetknob.setValueAt(valuez, x, 2)
        print 'frame:', x, '   X:',valuex, '   Y:',valuey, '   Z:',valuez
        x += 1



def curveGenBakeTransform():

    This = nuke.thisNode()
    xps = This['xpos'].value()
    yps = This['ypos'].value()
    nuke.root().begin()
    target = nuke.nodes.Transform(name=This.name()+'_2DBaked', xpos=xps+100, ypos = yps)

    targetknob = target['translate']
    targetknob.setAnimated()
    
    
    #BAKING ANIMATION
    x = nuke.root().firstFrame()
    while x <= nuke.root().lastFrame():
        valuex = This['CURVE'].valueAt(x)[0]
        valuey = This['CURVE'].valueAt(x)[1]
        valuez = This['CURVE'].valueAt(x)[2]
        targetknob.setValueAt(valuex, x, 0)
        targetknob.setValueAt(valuey, x, 1)
        targetknob.setValueAt(valuez, x, 2)
        print 'frame:', x, '   X:',valuex, '   Y:',valuey, '   Z:',valuez
        x += 1
        
        
        
def curveGenBake():

    This = nuke.thisNode()
    xps = This['xpos'].value()
    yps = This['ypos'].value()

    targetknob = This['Baked']
    targetknob.setAnimated()
    
    
    #BAKING ANIMATION
    x = nuke.root().firstFrame()
    while x <= nuke.root().lastFrame():
        valuex = This['CURVE'].valueAt(x)[0]
        valuey = This['CURVE'].valueAt(x)[1]
        valuez = This['CURVE'].valueAt(x)[2]
        targetknob.setValueAt(valuex, x, 0)
        targetknob.setValueAt(valuey, x, 1)
        targetknob.setValueAt(valuez, x, 2)
        print 'frame:', x, '   X:',valuex, '   Y:',valuey, '   Z:',valuez
        x += 1