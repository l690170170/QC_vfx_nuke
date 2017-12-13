import nuke
import os
import sys

def CreatePRX():
    
    node = nuke.thisNode()
    if node.Class() != 'Read':
        print 'No read node selected'
    else:
        #creating controller window
        class dialog ( object ):
            window = nuke.Panel("Create Proxy")
            window.addSingleLineInput('Time Range',  '%s-%s' % (nuke.root().firstFrame(), nuke.root().lastFrame()))
            window.addEnumerationPulldown("Render to:", "SameFolder Pick nukeTempFolder")
            window.addSingleLineInput("scale", 100)
            window.addEnumerationPulldown("Reformat Filter:", "Cubic Impulse Keys Simon Rifman Mitchell Parzen Notch")

    
        dialogResult = dialog.window.show()
    
        if dialogResult == 1:
            nuke.tprint("Creating Proxy")
        else:
            nuke.tprint("Canceled")
            return None
    
        #Extracting source path
        sourceFile = node.knob('file').getValue()
        tempPath = sourceFile.split('/')
        sourcePath = ""
        for i in range(0, len(tempPath) - 1):
            sourcePath += tempPath[i] + "/"
        
        #Extracting file name
        sourceFileName = sourceFile.split('/')[ - 1]
        fileNameTable = sourceFileName.split('.')
        
        if fileNameTable[-1] == 'mov':
            fileNameTable.pop()[-1]
            newFileName = fileNameTable[0]
            newFileName += '_####.jpg'
        else:
            fileNameTable.pop()[-1]
            newFileName = fileNameTable[0]
            newFileName += '.jpg'
    
        #Determining write path
        if dialog.window.value("Render to:") == "SameFolder":
            newPath = sourcePath + "_JPG/"
            try:
                os.mkdir(newPath)
            except:
                nuke.tprint("Render Folder already exists!")
        elif dialog.window.value("Render to:") == "Pick":
            newPath = nuke.getClipname('Get Sequence')
        else:
            newPath = (os.environ['NUKE_TEMP_DIR']) + "/_JPG/"
            try:
                os.mkdir(newPath)
            except:
                nuke.tprint("Render Folder already exists!") 
    
        #extracting frames
        timelist = dialog.window.value('Time Range').split('-')
        start = int(timelist[0])
        end = int(timelist[-1])
    
        print newPath + newFileName
    
        #Create temp nodes
        if int(dialog.window.value("scale")) != 100:
            nuke.nodes.Reformat(name = "tmpReformat", type = 2, scale = float(dialog.window.value("scale"))/100, filter = dialog.window.value("Reformat Filter:")).setInput(0, node)
            nuke.nodes.Write(name = 'tmpWrite', file = (newPath + newFileName), file_type = "jpeg", afterRender = ("nuke.delete(nuke.toNode('tmpReformat')), nuke.delete(nuke.thisNode())")).setInput(0, nuke.toNode('tmpReformat'))
        else:
            nuke.nodes.Write(name = 'tmpWrite', file = (newPath + newFileName), file_type = "jpeg", afterRender = ("nuke.delete(nuke.thisNode())")).setInput(0, node)
    
    
        
        #doing the thing
        nuke.execute ("tmpWrite", start, end, 1)
        node['proxy'].setValue(newPath + newFileName)
        print "writing" , newPath + newFileName , "(" , start , "_" , end , ")"
    
    
####################################################################################
####################################################################################

def CreatePRX_toolbar():
    
    node = nuke.selectedNode()
    if node.Class() != 'Read':
        print 'No read node selected'
    else:
        #creating controller window
        class dialog ( object ):
            window = nuke.Panel("Create Proxy")
            window.addSingleLineInput('Time Range',  '%s-%s' % (nuke.root().firstFrame(), nuke.root().lastFrame()))
            window.addEnumerationPulldown("Render to:", "SameFolder Pick nukeTempFolder")
            window.addSingleLineInput("scale", 100)
            window.addEnumerationPulldown("Reformat Filter:", "Cubic Impulse Keys Simon Rifman Mitchell Parzen Notch")

    
        dialogResult = dialog.window.show()
    
        if dialogResult == 1:
            nuke.tprint("Creating Proxy")
        else:
            nuke.tprint("Canceled")
            return None
    
        #Extracting source path
        sourceFile = node.knob('file').getValue()
        tempPath = sourceFile.split('/')
        sourcePath = ""
        for i in range(0, len(tempPath) - 1):
            sourcePath += tempPath[i] + "/"
        
        #Extracting file name
        sourceFileName = sourceFile.split('/')[ - 1]
        fileNameTable = sourceFileName.split('.')
        
        if fileNameTable[-1] == 'mov':
            fileNameTable.pop()[-1]
            newFileName = fileNameTable[0]
            newFileName += '_####.jpg'
        else:
            fileNameTable.pop()[-1]
            newFileName = fileNameTable[0]
            newFileName += '.jpg'
    
        #Determining write path
        if dialog.window.value("Render to:") == "SameFolder":
            newPath = sourcePath + "_JPG/"
            try:
                os.mkdir(newPath)
            except:
                nuke.tprint("Render Folder already exists!")
        elif dialog.window.value("Render to:") == "Pick":
            newPath = nuke.getClipname('Get Sequence')
        else:
            newPath = (os.environ['NUKE_TEMP_DIR']) + "/_JPG/"
            try:
                os.mkdir(newPath)
            except:
                nuke.tprint("Render Folder already exists!") 
    
        #extracting frames
        timelist = dialog.window.value('Time Range').split('-')
        start = int(timelist[0])
        end = int(timelist[-1])
    
        print newPath + newFileName
    
        #Create temp nodes
        if int(dialog.window.value("scale")) != 100:
            nuke.nodes.Reformat(name = "tmpReformat", type = 2, scale = float(dialog.window.value("scale"))/100, filter = dialog.window.value("Reformat Filter:")).setInput(0, node)
            nuke.nodes.Write(name = 'tmpWrite', file = (newPath + newFileName), file_type = "jpeg", afterRender = ("nuke.delete(nuke.toNode('tmpReformat')), nuke.delete(nuke.thisNode())")).setInput(0, nuke.toNode('tmpReformat'))
        else:
            nuke.nodes.Write(name = 'tmpWrite', file = (newPath + newFileName), file_type = "jpeg", afterRender = ("nuke.delete(nuke.thisNode())")).setInput(0, node)
    
    
        
        #doing the thing
        nuke.execute ("tmpWrite", start, end, 1)
        node['proxy'].setValue(newPath + newFileName)
        print "writing" , newPath + newFileName , "(" , start , "_" , end , ")"
    
    
####################################################################################
####################################################################################
#Create Read From Write

def PlusRFW():
    x=((nuke.thisNode()['file']).value())
    xps = ((nuke.thisNode()['xpos']).value())
    yps = ((nuke.thisNode()['ypos']).value())
    print "\nCreating read from " + x
    target = nuke.nodes.Read( file =  x, xpos=xps+100, ypos=yps)
    target['first'].setValue(int(nuke.root()['first_frame'].value()))
    target['origfirst'].setValue(int(nuke.root()['first_frame'].value()))
    target['last'].setValue(int(nuke.root()['last_frame'].value()))
    target['origlast'].setValue(int(nuke.root()['last_frame'].value()))


def PlusRFWLink():
    x=((nuke.thisNode()['name']).value())
    xps = ((nuke.thisNode()['xpos']).value())
    yps = ((nuke.thisNode()['ypos']).value())
    print "\nCreating read from " + x
    target = nuke.nodes.Read( file =  "[knob " + x +".file]", xpos=xps+100, ypos=yps)
    target['first'].setValue(int(nuke.root()['first_frame'].value()))
    target['origfirst'].setValue(int(nuke.root()['first_frame'].value()))
    target['last'].setValue(int(nuke.root()['last_frame'].value()))
    target['origlast'].setValue(int(nuke.root()['last_frame'].value()))

def PlusRFWLink_toolbar():
    node = nuke.selectedNode()
    if node.Class() != 'Write':
        nuke.message('Please select a Write node')
    else:
        xps = node['xpos'].value()
        yps = node['ypos'].value()
        knob=node['name'].value()
        print "\nCreating read from " + knob
        target = nuke.nodes.Read( file =  "[knob " + knob +".file]", xpos=xps+100, ypos=yps) 
        target['first'].setValue(int(nuke.root()['first_frame'].value()))
        target['origfirst'].setValue(int(nuke.root()['first_frame'].value()))
        target['last'].setValue(int(nuke.root()['last_frame'].value()))
        target['origlast'].setValue(int(nuke.root()['last_frame'].value()))

####################################################################################
####################################################################################




def PlusCrop():
    #Variables
    target = nuke.selectedNode()
    bbox = target.bbox()
    origname = target.name()
    

    #Creating the crop
    pluscrop = nuke.nodes.Crop(name=(origname +'_Crop'), reformat=1)
    pluscrop.setInput(0, target)
    
    #Setting values through expression
    pluscrop['box'].setExpression("input0.bbox.x()",0)
    pluscrop['box'].setExpression("input0.bbox.y()",1)
    pluscrop['box'].setExpression("input0.bbox.r()",2)
    pluscrop['box'].setExpression("input0.bbox.t()",3)
            
    #Selecting the new crop node
    for each in nuke.allNodes():
        each.knob("selected").setValue(False)
    pluscrop.knob('selected').setValue(True)
    pluscrop.showControlPanel()
    nuke.connectViewer(0,pluscrop)


