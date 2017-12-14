import nuke

####################################################################################

def whatClass():
    try:
        node = nuke.selectedNode()
        nuke.message('Node Class is:\n'+ node.Class() )
    except:
        nuke.message('Please select a node')

 
####################################################################################
                
def NodesColor():
    userColor = nuke.getColor()
    for i in nuke.selectedNodes():
        i.knob('tile_color').setValue(userColor)
        
####################################################################################      
        
def rgbToHex():
    rgbColor = nuke.getColor()
    print rgbColor
    nuke.message ( "Hex Value = " + str(rgbColor) )
        
        
####################################################################################

def AddLabel():
    #ADD LABEL TO SELECTED NODES
    txt = nuke.getInput('Change label', 'new label')
    if txt:
        for n in nuke.selectedNodes():
            n['label'].setValue(txt)
            
            
def RemoveLabel():
    for n in nuke.selectedNodes():
        n['label'].setValue('')
        
####################################################################################

def addIcons():
    if not nuke.selectedNodes():
        mynodes = nuke.allNodes()
    else:  
        mynodes = nuke.selectedNodes()
    path = nuke.getFilename('file name string', '*.png;*.jpg;*.jpeg;*.tif;*.tiff')
    for i in mynodes:
        i.knob('icon').setValue(path)
        
def removeIcons():
    if not nuke.selectedNodes():
        mynodes = nuke.allNodes()
    else:  
        mynodes = nuke.selectedNodes()
    for each in mynodes:
        each.knob('icon').setValue('0')
        
def copyIcons():

    opList = nuke.selectedNodes()
    copyList = []

    if opList.__len__() < 2:
        print "select two or more nodes"
    else:
        copyList.append(opList[-1])
        [i.knob('icon').setValue(copyList[-1].knob('icon').value()) for i in opList]
        
        
#################################################################################### 