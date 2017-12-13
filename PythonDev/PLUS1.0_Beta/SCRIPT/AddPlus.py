import nuke
import nukescripts
import sys
import os
import errno

####################################################################################   
####################################################################################
#allow nuke write to create folders

def createWriteDir():
  file = nuke.filename(nuke.thisNode())
  dir = os.path.dirname( file )
  osdir = nuke.callbacks.filenameFilter( dir )
  try:
    os.makedirs( osdir )
  except OSError, e:
    if e.errno != errno.EEXIST:
      raise
nuke.addBeforeRender(createWriteDir)

#######################################################################################
#######################################################################################

def plusFramehold():
    This = nuke.thisNode()
    tab = nuke.Tab_Knob('plus', 'plus')
    button = nuke.PyScript_Knob("STCF", "Set To Current Frame")
    This.addKnob(tab)
    This.addKnob(button)
    This.knob('first_frame').setValue(nuke.frame())
    This['STCF'].setCommand("pfh = nuke.thisNode().knob('first_frame').setValue(nuke.frame())")
nuke.addOnUserCreate(plusFramehold, nodeClass="FrameHold")

#######################################################################################
#######################################################################################

def plusRead():
    This = nuke.thisNode()
    tab = nuke.Tab_Knob('plus', 'plus')
    line1 = nuke.Text_Knob("PlusControl", "Plus Control")
    PRXbutton = nuke.PyScript_Knob("PRX", "Create proxy")
    OPNbutton = nuke.PyScript_Knob("OPN", "Open Directory")
    OPNbutton.setFlag(nuke.STARTLINE)
    rltvbutton = nuke.PyScript_Knob("rltv", "Relative")
    rltvbutton.setFlag(nuke.STARTLINE)
    obslbutton = nuke.PyScript_Knob("obsl", "obsolute")
    obslbutton.clearFlag(nuke.STARTLINE)
    
    This.addKnob(tab)
    This.addKnob(line1)
    This.addKnob(PRXbutton)
    This.addKnob(OPNbutton)
    This.addKnob(rltvbutton)
    This.addKnob(obslbutton)
    
    This['PRX'].setCommand('CreatePRX()')
    This['OPN'].setCommand('plusOpen()')
    This['rltv'].setCommand('make_relative()')
    This['obsl'].setCommand('make_obsolute()')
    
    
nuke.addOnUserCreate(plusRead, nodeClass="Read")

#################################################################################################
#################################################################################################

def plusCamera():
    This = nuke.thisNode()
    tab = nuke.Tab_Knob('plus', 'plus')
    check = This.knob('plus')
    if check is not None:
        pass
    else: 
        button = nuke.PyScript_Knob("BKUP", "Bake")
        button2 = nuke.PyScript_Knob("stereoRig", "Stereo Rig")
        button2.setFlag(nuke.STARTLINE)
        for k in (tab, button, button2):
            This.addKnob(k)
            
        This['BKUP'].setCommand('BakeUnderParent()')
        This['stereoRig'].setCommand('stereoRig()')
nuke.addOnUserCreate(plusCamera, nodeClass="Camera2")

#######################################################################################
##########################################################################

def plusCornerpin():
    This = nuke.thisNode()
    tab = nuke.Tab_Knob('plus', 'plus')
    button1 = nuke.PyScript_Knob("referenceF", "Set Refecence Frame")
    seperator = nuke.Text_Knob("Convert", "Convert")
    button2 = nuke.PyScript_Knob("CPMX", "CornerPin to Matrix")
    button3 = nuke.PyScript_Knob("MXCP", "Matrix to CornerPin")

    check = This.knob('plus')
    if check is not None:
        pass
    else:
        This.addKnob(tab)
        This.addKnob(button1)
        This.addKnob(seperator)
        This.addKnob(button2)
        This.addKnob(button3)
        This['referenceF'].setCommand('copyCurrent()')
        This['CPMX'].setCommand('CP_to_Matrix()')
        This['MXCP'].setCommand('Matrix_to_CP()')
        
nuke.addOnCreate(plusCornerpin, nodeClass="CornerPin2D")

##########################################################################
##########################################################################

def plusWrite():
    This = nuke.thisNode()
    tab = nuke.Tab_Knob('plus', 'plus')
    line1 = nuke.Text_Knob("PlusControl", "Plus Control")
    
    OPNbutton = nuke.PyScript_Knob("OPN", "Open Directory")
    OPNbutton.setFlag(nuke.STARTLINE)
    rfwbutton = nuke.PyScript_Knob("rfw", "Read from write")
    rfwbutton.setFlag(nuke.STARTLINE)
    linkCheck = nuke.Boolean_Knob("lnk", "Link")
    linkCheck.clearFlag(nuke.STARTLINE)
    
    This.addKnob(tab)
    This.addKnob(line1)
    This.addKnob(OPNbutton)
    This.addKnob(rfwbutton)
    This.addKnob(linkCheck)
    
    This['OPN'].setCommand('plusOpen()')
    
    def lnkv():
        if This['lnk'].value() == False:
            This['rfw'].setCommand('PlusRFW()')
        else:
            This['rfw'].setCommand('PlusRFWLink()')
    nuke.addKnobChanged(lnkv, nodeClass="Write")
nuke.addOnUserCreate(plusWrite, nodeClass="Write")


##########################################################################
##########################################################################



def plusreadgeo():
    This = nuke.thisNode()
    tab = nuke.Tab_Knob('plus', 'plus')
    line1 = nuke.Text_Knob("PlusControl", "Plus Control")

    OPNbutton = nuke.PyScript_Knob("OPN", "Open Directory")
    OPNbutton.setFlag(nuke.STARTLINE)
    rltvbutton = nuke.PyScript_Knob("rltv", "Relative")
    rltvbutton.setFlag(nuke.STARTLINE)
    obslbutton = nuke.PyScript_Knob("obsl", "obsolute")
    obslbutton.clearFlag(nuke.STARTLINE)
    
    This.addKnob(tab)
    This.addKnob(line1)
    This.addKnob(OPNbutton)
    This.addKnob(rltvbutton)
    This.addKnob(obslbutton)

    This['OPN'].setCommand('plusOpen()')
    This['rltv'].setCommand('make_relative()')
    This['obsl'].setCommand('make_obsolute()')
nuke.addOnUserCreate(plusreadgeo, nodeClass="ReadGeo2")


##########################################################################
##########################################################################


def plusAxis():
    This = nuke.thisNode()
    tab = nuke.Tab_Knob('plus', 'plus')
    check = This.knob('plus')
    if check is not None:
        pass
    else: 
        button = nuke.PyScript_Knob("BKUP", "Bake")
        for k in (tab, button):
            This.addKnob(k)
            
        This['BKUP'].setCommand('BakeUnderParent()')
nuke.addOnUserCreate(plusAxis, nodeClass="Axis2")

#######################################################################################
##########################################################################
#ADD PLUS CONTROL TO OLD NODES

def addPlus():
    try:
        This = nuke.selectedNode()
        nodeClass = This.Class()
        tab = nuke.Tab_Knob('plus', 'plus')
        check = This.knob('plus')
        if check is not None:
            print 'knobs already exists'
            pass
        else: 
            if nodeClass == 'FrameHold':
                button = nuke.PyScript_Knob("STCF", "Set To Current Frame")
                This.addKnob(tab)
                This.addKnob(button)
                This.knob('first_frame').setValue(nuke.frame())
                This['STCF'].setCommand("pfh = nuke.thisNode().knob('first_frame').setValue(nuke.frame())")
            
            elif nodeClass == 'Read':
                line1 = nuke.Text_Knob("PlusControl", "Plus Control")
                PRXbutton = nuke.PyScript_Knob("PRX", "Create proxy")
                OPNbutton = nuke.PyScript_Knob("OPN", "Open Directory")
                OPNbutton.setFlag(nuke.STARTLINE)
                rltvbutton = nuke.PyScript_Knob("rltv", "Relative")
                rltvbutton.setFlag(nuke.STARTLINE)
                obslbutton = nuke.PyScript_Knob("obsl", "obsolute")
                obslbutton.clearFlag(nuke.STARTLINE)
                
                This.addKnob(tab)
                This.addKnob(line1)
                This.addKnob(PRXbutton)
                This.addKnob(OPNbutton)
                This.addKnob(rltvbutton)
                This.addKnob(obslbutton)
                
                This['PRX'].setCommand('CreatePRX()')
                This['OPN'].setCommand('plusOpen()')
                This['rltv'].setCommand('make_relative()')
                This['obsl'].setCommand('make_obsolute()')
            
            elif nodeClass == 'Camera2':
                check = This.knob('plus')
                if check is not None:
                    pass
                else: 
                    button = nuke.PyScript_Knob("BKUP", "Bake")
                    button2 = nuke.PyScript_Knob("stereoRig", "Stereo Rig")
                    button2.setFlag(nuke.STARTLINE)
                    for k in (tab, button, button2):
                        This.addKnob(k)
                    This['BKUP'].setCommand('BakeUnderParent()')
                    This['stereoRig'].setCommand('stereoRig()')
            
            elif nodeClass == 'CornerPin2D':
                button1 = nuke.PyScript_Knob("referenceF", "Set Refecence Frame")
                seperator = nuke.Text_Knob("Convert", "Convert")
                button2 = nuke.PyScript_Knob("CPMX", "CornerPin to Matrix")
                button3 = nuke.PyScript_Knob("MXCP", "Matrix to CornerPin")
                This.addKnob(tab)
                This.addKnob(button1)
                This.addKnob(seperator)
                This.addKnob(button2)
                This.addKnob(button3)
                This['referenceF'].setCommand('copyCurrent()')
                This['CPMX'].setCommand('CP_to_Matrix()')
                This['MXCP'].setCommand('Matrix_to_CP()')
            
            elif nodeClass == 'Write':
                line1 = nuke.Text_Knob("PlusControl", "Plus Control")
                OPNbutton = nuke.PyScript_Knob("OPN", "Open Directory")
                OPNbutton.setFlag(nuke.STARTLINE)
                rfwbutton = nuke.PyScript_Knob("rfw", "Read from write")
                rfwbutton.setFlag(nuke.STARTLINE)
                linkCheck = nuke.Boolean_Knob("lnk", "Link")
                linkCheck.clearFlag(nuke.STARTLINE)
                This.addKnob(tab)
                This.addKnob(line1)
                This.addKnob(OPNbutton)
                This.addKnob(rfwbutton)
                This.addKnob(linkCheck)
                This['OPN'].setCommand('plusOpen()')
                def lnkv():
                    if This['lnk'].value() == False:
                        This['rfw'].setCommand('PlusRFW()')
                    else:
                        This['rfw'].setCommand('PlusRFWLink()')
                nuke.addKnobChanged(lnkv, nodeClass="Write")
            
            elif nodeClass == 'ReadGeo2':
                line1 = nuke.Text_Knob("PlusControl", "Plus Control")
                OPNbutton = nuke.PyScript_Knob("OPN", "Open Directory")
                OPNbutton.setFlag(nuke.STARTLINE)
                rltvbutton = nuke.PyScript_Knob("rltv", "Relative")
                rltvbutton.setFlag(nuke.STARTLINE)
                obslbutton = nuke.PyScript_Knob("obsl", "obsolute")
                obslbutton.clearFlag(nuke.STARTLINE)
                
                This.addKnob(tab)
                This.addKnob(line1)
                This.addKnob(OPNbutton)
                This.addKnob(rltvbutton)
                This.addKnob(obslbutton)
            
                This['OPN'].setCommand('plusOpen()')
                This['rltv'].setCommand('make_relative()')
                This['obsl'].setCommand('make_obsolute()')
            
            elif nodeClass == 'Axis2':
                button = nuke.PyScript_Knob("BKUP", "Bake")
                for k in (tab, button):
                    This.addKnob(k)
                This['BKUP'].setCommand('BakeUnderParent()')
    
            else:
                print "\nThere aren't any control knobs available for this class "
    except:
        print "no node selected"   
        
        
  
