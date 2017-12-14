import nuke
import nukescripts
import math

#######################################################################################
#BAKE CAMERA UNDER PARENT'

def BakeUnderParent():
    #DEFINING VARIABLES
    node = nuke.selectedNode()
    nodeClass = node.Class()
    knob = node.knob('world_matrix')
    sourceMatrix = nuke.math.Matrix4()
    xps = node['xpos'].value()
    yps = node['ypos'].value()
    
    def bakeIt():
        #FRAME RANGE
        timerange = nuke.getFramesAndViews('Get Frame Range',  '%s-%s' %(nuke.root().firstFrame(), nuke.root().lastFrame()) )
        frange = nuke.FrameRange(timerange[0])
        #GETTING MAIN MATRIX
        for i in frange:
            knobValue = knob.valueAt(i)
            for each in range(0,16):
                sourceMatrix[each]=knobValue[each]
            sourceMatrix.transpose()
        
        
            #SCALE MATRIX
            smatrix = nuke.math.Matrix4(sourceMatrix)
            smatrix.scaleOnly()
            #SCALE VALUES
            scaleX = smatrix[0]
            scaleY = smatrix[5]
            scaleZ = smatrix[10]
        
            #ROTATION MATRIX
            rmatrix = nuke.math.Matrix4(sourceMatrix)
            rmatrix.rotationOnly()
            rmatrixv = rmatrix.rotationsZXY()
            #ROTATION VALUES
            degreeX = math.degrees(rmatrixv[0])
            degreeY = math.degrees(rmatrixv[1])
            degreeZ = math.degrees(rmatrixv[2])
        
            #TRANSLATION MATRIX
            tmatrix = nuke.math.Matrix4(sourceMatrix)
            tmatrix.translationOnly()
            #TRANSLATION VALUES
            translateX = tmatrix[12]
            translateY = tmatrix[13]
            translateZ = tmatrix[14]
        
            #PRINTING
            print '\ntranslateX: ','x=',translateX,'','Y=',translateY,'','Z=',translateZ
            print '\nrotate: ','x=',degreeX,'','y=',degreeY,'','z=',degreeZ
            print '\nscale: ','x=',scaleX,'','y=',scaleY,'','z=',scaleZ
            
            #SETTING VALUES
            for each in (target['translate'],target['rotate'],target['scaling']):
                each.setAnimated()
            target['translate'].setValueAt(translateX, i, 0)
            target['translate'].setValueAt(translateY, i, 1)
            target['translate'].setValueAt(translateZ, i, 2)
            target['rotate'].setValueAt(degreeX, i, 0)
            target['rotate'].setValueAt(degreeY, i, 1)
            target['rotate'].setValueAt(degreeZ, i, 2)
            target['scaling'].setValueAt(scaleX, i, 0)
            target['scaling'].setValueAt(scaleY, i, 1)
            target['scaling'].setValueAt(scaleZ, i, 2)
    
    #CREATING BAKED NODE
    if nodeClass == 'Camera2':
        target = nuke.nodes.Camera2(name=(node['name'].value())+'_Baked', xpos=xps+100, ypos=yps)
        bakeIt()
    elif nodeClass == 'Axis2':
        target = nuke.nodes.Axis2(name=(node['name'].value())+'_Baked', xpos=xps+100, ypos=yps)
        bakeIt()
    else:
        nuke.message('select either a Camera or an Axis node')
        pass
    
#######################################################################################
#######################################################################################
#CREATE STEREO RIG FROM CAMERA

def stereoRig():
    
    nukescripts.stereo.setViewsForStereo()
    #ACCESSING TARGET NODE
    target = nuke.thisNode()
    if target.Class() != 'Camera2':
        nuke.message('select a camera node')
        pass
    else:
        targetx = target['xpos'].value()
        targety = target['ypos'].value()
        #ADJUSTING TARGET KNOBS
        try:
            knob = target['BKUP']
            knob2 = target['stereoRig']
            knob3 = target['plus']
            target.removeKnob(knob)
            target.removeKnob(knob2)
            target.removeKnob(knob3)
        except:
            pass
        #CREATE STEREO TAB
        stereotab = nuke.Tab_Knob('StereoRig', 'Stereo Rig')
        IPDSlider = nuke.Double_Knob('IPD', 'Interpupillary Distance')
        IPDSlider.setFlag(nuke.STARTLINE)
        IPDSlider.setRange(52,78)
        convergence = nuke.Double_Knob('convergence', 'Convergence Point')
        convergence.setFlag(nuke.STARTLINE)
        convergence.setRange(1,1000)
        hshift = nuke.Double_Knob('Hshift', 'Hshift')
        hshift.setRange(-100,100)
        hshift.setFlag(nuke.STARTLINE)
        vshift = nuke.Double_Knob('Vshift', 'Vshift')
        vshift.setFlag(nuke.STARTLINE)
        vshift.setRange(-100,100)
        targeted = nuke.Enumeration_Knob('targeted', 'Targeted Camera', ['free', 'targeted'])
        MAINCAMLIST = [stereotab, targeted, IPDSlider, convergence, hshift, vshift]
        for k in MAINCAMLIST:
            target.addKnob(k)
        target['IPD'].setValue(65)
        target['convergence'].setValue(250)
        
        #CREATE RIGHT CAMERA
        CAM__RIGHT = nuke.nodes.Camera2 (name=target.name()+"__RIGHT", xpos = targetx +220, ypos = targety+75)
        #RIGHT CAM NODE PARAMETERS
        CAM__RIGHT.setInput(0, target)
        CAM__RIGHT['translate'].setExpression(target.name()+'.IPD/20+'+target.name()+'.Hshift', 0)
        CAM__RIGHT['translate'].setExpression(target.name()+'.Vshift', 1)
        hexCameraRight = int('%02x%02x%02x%02x' % (0*255,1*255,0*255,1),16)
        CAM__RIGHT['tile_color'].setValue(hexCameraRight)
        CAM__RIGHT['focal'].setExpression(target.name() + '.focal')
        CAM__RIGHT['haperture'].setExpression(target.name() + '.haperture')
        CAM__RIGHT['vaperture'].setExpression(target.name() + '.vaperture')
        CAM__RIGHT['near'].setExpression(target.name() + '.near')
        CAM__RIGHT['far'].setExpression(target.name() + '.far')
        CAM__RIGHT['win_translate'].setExpression(target.name() + '.win_translate')
        CAM__RIGHT['win_scale'].setExpression(target.name() + '.win_scale')
        CAM__RIGHT['winroll'].setExpression(target.name() + '.winroll')
        CAM__RIGHT['focal_point'].setExpression(target.name() + '.focal_point')
        CAM__RIGHT['fstop'].setExpression(target.name() + '.fstop')
        CAM__RIGHT['look_rotate_x'].setValue(0)
        CAM__RIGHT['look_rotate_z'].setValue(0)
        
        #CREATE LEFT CAMERA
        CAM__LEFT = nuke.nodes.Camera2 (name=target.name()+"__LEFT", xpos = targetx -220, ypos = targety+75)
        #LEFT CAM NODE PARAMETERS
        CAM__LEFT.setInput(0, target)
        CAM__LEFT['translate'].setExpression('-1*'+target.name()+'.IPD/20+'+target.name()+'.Hshift', 0)
        CAM__LEFT['translate'].setExpression(target.name()+'.Vshift', 1)
        hexCameraLeft = int('%02x%02x%02x%02x' % (1*255,0*255,0*255,1),16)
        CAM__LEFT['tile_color'].setValue(hexCameraLeft)
        CAM__LEFT['focal'].setExpression(target.name() + '.focal')
        CAM__LEFT['haperture'].setExpression(target.name() + '.haperture')
        CAM__LEFT['vaperture'].setExpression(target.name() + '.vaperture')
        CAM__LEFT['near'].setExpression(target.name() + '.near')
        CAM__LEFT['far'].setExpression(target.name() + '.far')
        CAM__LEFT['win_translate'].setExpression(target.name() + '.win_translate')
        CAM__LEFT['win_scale'].setExpression(target.name() + '.win_scale')
        CAM__LEFT['winroll'].setExpression(target.name() + '.winroll')
        CAM__LEFT['focal_point'].setExpression(target.name() + '.focal_point')
        CAM__LEFT['fstop'].setExpression(target.name() + '.fstop')
        CAM__LEFT['look_rotate_x'].setValue(0)
        CAM__LEFT['look_rotate_z'].setValue(0)
        
        
        #NODES POSITIONS
        CAM__RIGHTX = CAM__RIGHT['xpos'].value()
        CAM__RIGHTY = CAM__RIGHT['ypos'].value()
        CAM__LEFTX = CAM__LEFT['xpos'].value()
        CAM__LEFTY = CAM__LEFT['ypos'].value()
        nodeWidth = target.screenWidth()/2
        DOT1xpos = CAM__RIGHTX + nodeWidth
        DOT2xpos = CAM__LEFTX + nodeWidth
        #CREATING DOTS
        DOT_RIGHT = nuke.nodes.Dot(xpos = DOT1xpos-6, ypos = CAM__RIGHTY -200)
        DOT_LEFT = nuke.nodes.Dot(xpos = DOT2xpos-6, ypos = CAM__LEFTY -200)
        #CONNECTING CAMERAS TO DOTS
        CAM__LEFT.setInput(1, DOT_LEFT)
        CAM__RIGHT.setInput(1, DOT_RIGHT)
        
        
        #CREATE CONVERGENCE POINT
        convergence = nuke.nodes.Axis2 (name = target.name()+'_ConvergencePoint', xpos = targetx , ypos = targety -250)
        DOT_RIGHT.setInput(0, convergence)
        DOT_LEFT.setInput(0, convergence)
        convergence.setInput(0, target)
        convergence['translate'].setExpression('0', 0)
        convergence['translate'].setExpression('0', 1)
        convergence['translate'].setExpression('-1*' + target.name() + '.convergence', 2)
        
        #CREATE CLOSEST OBJECT WARNING POINT
        ClosestObject = nuke.nodes.Axis2 (name = target.name()+'_ClosestObject', label = "1/30 Limit rule For reference only"
                                            , xpos = targetx +90 , ypos = targety -125)
        ClosestObject.setInput(0, target)
        ClosestObject['translate'].setExpression(target.name() + '.IPD/10 * -30', 2)
        for n in ClosestObject.allKnobs():
            n.setEnabled(False)
        
        
        #CREATE MAIN CAM DOT
        DOT_MAIN = nuke.nodes.Dot( xpos = targetx  +120 , ypos = targety +nodeWidth -40
                                    , label = 'Connect Camera \n animation here')
        target.setInput(0, DOT_MAIN)
        DOT_MAIN['hide_input'].setValue(1)
        hexDOT_MAIN = int('%02x%02x%02x%02x' % (1*255,0*255,1*255,1),16)
        DOT_MAIN.knob('tile_color').setValue(hexDOT_MAIN)
        hexfnDOT_MAIN = int('%02x%02x%02x%02x' % (1*255,1*255,1*255,1),16)
        DOT_MAIN.knob('note_font_color').setValue(hexfnDOT_MAIN)
        
        
        #CREATE TARGET SWITCH
        targetswitch = nuke.nodes.Switch(name = target.name()+'_TargetSwitch',
                                         xpos = targetx  -110 , ypos = targety +nodeWidth -30)
        target.setInput(1, targetswitch)
        targetswitch['which'].setExpression(target.name()+'.targeted')
        
        #CREATE TARGET NODE
        targetnode = nuke.nodes.Axis2 (name = target.name()+'_Target', xpos = targetx -100, ypos = targety +nodeWidth -150)
        targetswitch.setInput(1, targetnode)
        hex_MAIN = int('%02x%02x%02x%02x' % (0.5*255,0.5*255,0.5*255,1),16)
        target.knob('tile_color').setValue(hex_MAIN)
        targetnode.knob('tile_color').setValue(hex_MAIN)
        targetPOSx = target['translate'].getValue(0)
        targetPOSy = target['translate'].getValue(1)
        targetPOSz = target['translate'].getValue(2)
        targetnode['translate'].setValue(targetPOSx, 0)
        targetnode['translate'].setValue(targetPOSy, 1)
        targetnode['translate'].setValue(targetPOSz, 2)
        
        
    
#######################################################################################
#######################################################################################
def stereoRig_toolbar():
    
    nukescripts.stereo.setViewsForStereo()
    #ACCESSING TARGET NODE
    target = nuke.selectedNode()
    if target.Class() != 'Camera2':
        nuke.message('select a camera node')
        pass
    else:
        targetx = target['xpos'].value()
        targety = target['ypos'].value()
        #ADJUSTING TARGET KNOBS
        try:
            knob = target['BKUP']
            knob2 = target['stereoRig']
            knob3 = target['plus']
            target.removeKnob(knob)
            target.removeKnob(knob2)
            target.removeKnob(knob3)
        except:
            pass
        #CREATE STEREO TAB
        stereotab = nuke.Tab_Knob('StereoRig', 'Stereo Rig')
        IPDSlider = nuke.Double_Knob('IPD', 'Interpupillary Distance')
        IPDSlider.setFlag(nuke.STARTLINE)
        IPDSlider.setRange(52,78)
        convergence = nuke.Double_Knob('convergence', 'Convergence Point')
        convergence.setFlag(nuke.STARTLINE)
        convergence.setRange(1,1000)
        hshift = nuke.Double_Knob('Hshift', 'Hshift')
        hshift.setRange(-100,100)
        hshift.setFlag(nuke.STARTLINE)
        vshift = nuke.Double_Knob('Vshift', 'Vshift')
        vshift.setFlag(nuke.STARTLINE)
        vshift.setRange(-100,100)
        targeted = nuke.Enumeration_Knob('targeted', 'Targeted Camera', ['free', 'targeted'])
        MAINCAMLIST = [stereotab, targeted, IPDSlider, convergence, hshift, vshift]
        for k in MAINCAMLIST:
            target.addKnob(k)
        target['IPD'].setValue(65)
        target['convergence'].setValue(250)
        
        #CREATE RIGHT CAMERA
        CAM__RIGHT = nuke.nodes.Camera2 (name=target.name()+"__RIGHT", xpos = targetx +220, ypos = targety+75)
        #RIGHT CAM NODE PARAMETERS
        CAM__RIGHT.setInput(0, target)
        CAM__RIGHT['translate'].setExpression(target.name()+'.IPD/20+'+target.name()+'.Hshift', 0)
        CAM__RIGHT['translate'].setExpression(target.name()+'.Vshift', 1)
        hexCameraRight = int('%02x%02x%02x%02x' % (0*255,1*255,0*255,1),16)
        CAM__RIGHT['tile_color'].setValue(hexCameraRight)
        CAM__RIGHT['focal'].setExpression(target.name() + '.focal')
        CAM__RIGHT['haperture'].setExpression(target.name() + '.haperture')
        CAM__RIGHT['vaperture'].setExpression(target.name() + '.vaperture')
        CAM__RIGHT['near'].setExpression(target.name() + '.near')
        CAM__RIGHT['far'].setExpression(target.name() + '.far')
        CAM__RIGHT['win_translate'].setExpression(target.name() + '.win_translate')
        CAM__RIGHT['win_scale'].setExpression(target.name() + '.win_scale')
        CAM__RIGHT['winroll'].setExpression(target.name() + '.winroll')
        CAM__RIGHT['focal_point'].setExpression(target.name() + '.focal_point')
        CAM__RIGHT['fstop'].setExpression(target.name() + '.fstop')
        CAM__RIGHT['look_rotate_x'].setValue(0)
        CAM__RIGHT['look_rotate_z'].setValue(0)
        
        #CREATE LEFT CAMERA
        CAM__LEFT = nuke.nodes.Camera2 (name=target.name()+"__LEFT", xpos = targetx -220, ypos = targety+75)
        #LEFT CAM NODE PARAMETERS
        CAM__LEFT.setInput(0, target)
        CAM__LEFT['translate'].setExpression('-1*'+target.name()+'.IPD/20+'+target.name()+'.Hshift', 0)
        CAM__LEFT['translate'].setExpression(target.name()+'.Vshift', 1)
        hexCameraLeft = int('%02x%02x%02x%02x' % (1*255,0*255,0*255,1),16)
        CAM__LEFT['tile_color'].setValue(hexCameraLeft)
        CAM__LEFT['focal'].setExpression(target.name() + '.focal')
        CAM__LEFT['haperture'].setExpression(target.name() + '.haperture')
        CAM__LEFT['vaperture'].setExpression(target.name() + '.vaperture')
        CAM__LEFT['near'].setExpression(target.name() + '.near')
        CAM__LEFT['far'].setExpression(target.name() + '.far')
        CAM__LEFT['win_translate'].setExpression(target.name() + '.win_translate')
        CAM__LEFT['win_scale'].setExpression(target.name() + '.win_scale')
        CAM__LEFT['winroll'].setExpression(target.name() + '.winroll')
        CAM__LEFT['focal_point'].setExpression(target.name() + '.focal_point')
        CAM__LEFT['fstop'].setExpression(target.name() + '.fstop')
        CAM__LEFT['look_rotate_x'].setValue(0)
        CAM__LEFT['look_rotate_z'].setValue(0)
        
        
        #NODES POSITIONS
        CAM__RIGHTX = CAM__RIGHT['xpos'].value()
        CAM__RIGHTY = CAM__RIGHT['ypos'].value()
        CAM__LEFTX = CAM__LEFT['xpos'].value()
        CAM__LEFTY = CAM__LEFT['ypos'].value()
        nodeWidth = target.screenWidth()/2
        DOT1xpos = CAM__RIGHTX + nodeWidth
        DOT2xpos = CAM__LEFTX + nodeWidth
        #CREATING DOTS
        DOT_RIGHT = nuke.nodes.Dot(xpos = DOT1xpos-6, ypos = CAM__RIGHTY -200)
        DOT_LEFT = nuke.nodes.Dot(xpos = DOT2xpos-6, ypos = CAM__LEFTY -200)
        #CONNECTING CAMERAS TO DOTS
        CAM__LEFT.setInput(1, DOT_LEFT)
        CAM__RIGHT.setInput(1, DOT_RIGHT)
        
        
        #CREATE CONVERGENCE POINT
        convergence = nuke.nodes.Axis2 (name = target.name()+'_ConvergencePoint', xpos = targetx , ypos = targety -250)
        DOT_RIGHT.setInput(0, convergence)
        DOT_LEFT.setInput(0, convergence)
        convergence.setInput(0, target)
        convergence['translate'].setExpression('0', 0)
        convergence['translate'].setExpression('0', 1)
        convergence['translate'].setExpression('-1*' + target.name() + '.convergence', 2)
        
        #CREATE CLOSEST OBJECT WARNING POINT
        ClosestObject = nuke.nodes.Axis2 (name = target.name()+'_ClosestObject', label = "1/30 Limit rule For reference only"
                                            , xpos = targetx +90 , ypos = targety -125)
        ClosestObject.setInput(0, target)
        ClosestObject['translate'].setExpression(target.name() + '.IPD/10 * -30', 2)
        for n in ClosestObject.allKnobs():
            n.setEnabled(False)
        
        
        #CREATE MAIN CAM DOT
        DOT_MAIN = nuke.nodes.Dot( xpos = targetx  +120 , ypos = targety +nodeWidth -40
                                    , label = 'Connect Camera \n animation here')
        target.setInput(0, DOT_MAIN)
        DOT_MAIN['hide_input'].setValue(1)
        hexDOT_MAIN = int('%02x%02x%02x%02x' % (1*255,0*255,1*255,1),16)
        DOT_MAIN.knob('tile_color').setValue(hexDOT_MAIN)
        hexfnDOT_MAIN = int('%02x%02x%02x%02x' % (1*255,1*255,1*255,1),16)
        DOT_MAIN.knob('note_font_color').setValue(hexfnDOT_MAIN)
        
        
        #CREATE TARGET SWITCH
        targetswitch = nuke.nodes.Switch(name = target.name()+'_TargetSwitch',
                                         xpos = targetx  -110 , ypos = targety +nodeWidth -30)
        target.setInput(1, targetswitch)
        targetswitch['which'].setExpression(target.name()+'.targeted')
        
        #CREATE TARGET NODE
        targetnode = nuke.nodes.Axis2 (name = target.name()+'_Target', xpos = targetx -100, ypos = targety +nodeWidth -150)
        targetswitch.setInput(1, targetnode)
        hex_MAIN = int('%02x%02x%02x%02x' % (0.5*255,0.5*255,0.5*255,1),16)
        target.knob('tile_color').setValue(hex_MAIN)
        targetnode.knob('tile_color').setValue(hex_MAIN)
        targetPOSx = target['translate'].getValue(0)
        targetPOSy = target['translate'].getValue(1)
        targetPOSz = target['translate'].getValue(2)
        targetnode['translate'].setValue(targetPOSx, 0)
        targetnode['translate'].setValue(targetPOSy, 1)
        targetnode['translate'].setValue(targetPOSz, 2)
        
        
    
#######################################################################################
#######################################################################################
#BAKE BUTTON COMMAND FOR (TRACK TO 3D) NODE


def bakeTrackTo3D():
    firstframe = nuke.Root()['first_frame'].value()
    lastframe = nuke.Root()['last_frame'].value()
    framelist = []
    xtm = firstframe
    while xtm <= lastframe :
        framelist.append(xtm)
        xtm +=1
    print framelist
    This = nuke.thisNode()
    xps = This['xpos'].value()
    yps = This['ypos'].value()
    This.end()
    target = nuke.nodes.Axis2(name=(This.knob('name').value())+'_Baked', xpos=xps+100, ypos=yps+100)
    
    try:
        camerainput = This.input(1)
        target.setInput(0,camerainput)
        target['hide_input'].setValue(True)
    except:
        pass
    targetT = target.knob('translate')
    targetT.setAnimated()
    nuke.activeViewer().frameControl(-6)
    for each in framelist:
        xn0 = This['OUTPUT'].getValueAt(each)[0]
        xn1 = This['OUTPUT'].getValueAt(each)[1]
        xn2 = This['OUTPUT'].getValueAt(each)[2]
        targetT.setValueAt(xn0, each, 0)
        targetT.setValueAt(xn1, each, 1)
        targetT.setValueAt(xn2, each, 2)
        
        
####################################################################################
####################################################################################
    

