import nuke, sys, os

####################################################################################
#CornerPin to Matrix

def CP_to_Matrix():

    node = nuke.thisNode()
    parentNode = node.input(0)
    imageWidth = float(node.width())
    imageHeight = float(node.height())
    xps = node['xpos'].value()
    yps = node['ypos'].value()
    
    #CREATING EMPTY MATRICES
    cornerPinMatrixTo = nuke.math.Matrix4()
    cornerPinMatrixFrom = nuke.math.Matrix4()
    
    #CREATING KNOBS
    baked = nuke.nodes.CornerPin2D(name=node.name()+'_Matrix', xpos=xps+100, ypos=yps)
    baked['from2'].setValue(imageWidth,0)
    baked['from3'].setValue(imageWidth,0)
    baked['from3'].setValue(imageHeight,1)
    baked['from4'].setValue(imageHeight,1)
    baked['to2'].setValue(imageWidth,0)
    baked['to3'].setValue(imageWidth,0)
    baked['to3'].setValue(imageHeight,1)
    baked['to4'].setValue(imageHeight,1)
    baked.setInput(0, parentNode)
    tab = nuke.Tab_Knob('plus', 'plus')
    switcher = nuke.Enumeration_Knob('switcher', 'Matrix Type', ['All', 'Scale Only', 'Rotation Only', 'Translate Only', 'ScaleAndRotate Only'])
    finalMatrixArr = nuke.Array_Knob('finalMatrixKnob', 'All', 16)
    mtxScaleArr = nuke.Array_Knob('mtxScaleKnob', 'Scale Only', 16)
    mtxRotationArr = nuke.Array_Knob('mtxRotationKnob', 'Rotation Only', 16)
    mtxTranslationArr = nuke.Array_Knob('mtxTranslationKnob', 'Translate Only', 16)
    mtxScaleRotationArr = nuke.Array_Knob('mtxScaleRotationKnob', 'ScaleAndRotate Only', 16)
    #ADDING KNOBS
    check = node.knob('plus')
    if check is not None:
        baked.addKnob(switcher)
        for each in (finalMatrixArr, mtxScaleArr, mtxRotationArr,  mtxTranslationArr, mtxScaleRotationArr):
            baked.addKnob(each)
            each.setVisible(False)
    else:
        baked.addKnob(tab)
        baked.addKnob(switcher)
        for each in (finalMatrixArr, mtxScaleArr, mtxRotationArr,  mtxTranslationArr, mtxScaleRotationArr):
            baked.addKnob(each)
            each.setVisible(False)
    
    #FRAME RANGE
    range = nuke.getFramesAndViews('Get Frame Range',  '%s-%s' %(nuke.root().firstFrame(), nuke.root().lastFrame()) )
    frange = nuke.FrameRange(range[0])
    
    for n in frange:
        #GETTING KNOBS VALUES
        vectorsTo = [nuke.math.Vector2(node[f].getValueAt(n)[0], node[f].getValueAt(n)[1]) for f in sorted(node.knobs().keys()) if f.startswith('to')]
        vectorsFrom = [nuke.math.Vector2(node[f].getValueAt(n)[0], node[f].getValueAt(n)[1]) for f in sorted(node.knobs().keys()) if f.startswith('from')]
        
        #CONVERTING CORNER PIN TO MATRICES
        cornerPinMatrixTo.mapUnitSquareToQuad(vectorsTo[0].x, vectorsTo[0].y, vectorsTo[1].x, vectorsTo[1].y, vectorsTo[2].x, vectorsTo[2].y, vectorsTo[3].x, vectorsTo[3].y)
        cornerPinMatrixFrom.mapUnitSquareToQuad(vectorsFrom[0].x, vectorsFrom[0].y, vectorsFrom[1].x, vectorsFrom[1].y, vectorsFrom[2].x, vectorsFrom[2].y, vectorsFrom[3].x, vectorsFrom[3].y)
        
        #FINAL MATRIX VALUE
        finalMatrix = cornerPinMatrixTo * cornerPinMatrixFrom.inverse()
        finalMatrix.transpose()
    
        #DERIVATIVES
        mtxRotation = nuke.math.Matrix4(finalMatrix)
        mtxRotation.rotationOnly()
        mtxScale = nuke.math.Matrix4(finalMatrix)
        mtxScale.scaleOnly()
        mtxTranslation = nuke.math.Matrix4(finalMatrix)
        mtxTranslation.translationOnly()
        mtxScaleRotation = nuke.math.Matrix4(finalMatrix)
        mtxScaleRotation.scaleAndRotationOnly()
        #SET ANIMATED
        baked['finalMatrixKnob'].setAnimated()
        baked['mtxScaleKnob'].setAnimated()
        baked['mtxRotationKnob'].setAnimated()
        baked['mtxTranslationKnob'].setAnimated()
        baked['mtxScaleRotationKnob'].setAnimated()
    
        #ASSIGNING MATRICES TO KNOBS
        knobsCount = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        
        [(baked['finalMatrixKnob'].setValueAt(finalMatrix[i], n, i)) for i in knobsCount]
        [(baked['mtxScaleKnob'].setValueAt(mtxScale[i], n, i)) for i in knobsCount]
        [(baked['mtxRotationKnob'].setValueAt(mtxRotation[i], n, i)) for i in knobsCount]
        [(baked['mtxTranslationKnob'].setValueAt(mtxTranslation[i], n, i)) for i in knobsCount]
        [(baked['mtxScaleRotationKnob'].setValueAt(mtxScaleRotation[i], n, i)) for i in knobsCount]
    
    baked['transform_matrix'].setExpression('finalMatrixKnob')
    print finalMatrix


def MatrixSwitchLink():
    n = nuke.thisNode()
    k = nuke.thisKnob()
    if k.name() == "switcher":
        if k.value() == 'All':
            n['transform_matrix'].setExpression('finalMatrixKnob')
        elif k.value() == 'Scale Only':
            n['transform_matrix'].setExpression('mtxScaleKnob')
        elif k.value() == 'Rotation Only':
            n['transform_matrix'].setExpression('mtxRotationKnob')
        elif k.value() == 'Translate Only':
            n['transform_matrix'].setExpression('mtxTranslationKnob')
        elif k.value() == 'ScaleAndRotate Only':
            n['transform_matrix'].setExpression('mtxScaleRotationKnob')
nuke.addKnobChanged(MatrixSwitchLink, nodeClass="CornerPin2D")


####################################################################################
####################################################################################

def CP_to_Matrix_toolbar():

    node = nuke.selectedNode()
    if node.Class() != 'CornerPin2D':
        nuke.message("please select a cornerpin node")
    else:
        parentNode = node.input(0)
        imageWidth = float(node.width())
        imageHeight = float(node.height())
        xps = node['xpos'].value()
        yps = node['ypos'].value()
        
        #CREATING EMPTY MATRICES
        cornerPinMatrixTo = nuke.math.Matrix4()
        cornerPinMatrixFrom = nuke.math.Matrix4()
        
        #CREATING KNOBS
        baked = nuke.nodes.CornerPin2D(name=node.name()+'_Matrix', xpos=xps+100, ypos=yps)
        baked['from2'].setValue(imageWidth,0)
        baked['from3'].setValue(imageWidth,0)
        baked['from3'].setValue(imageHeight,1)
        baked['from4'].setValue(imageHeight,1)
        baked['to2'].setValue(imageWidth,0)
        baked['to3'].setValue(imageWidth,0)
        baked['to3'].setValue(imageHeight,1)
        baked['to4'].setValue(imageHeight,1)
        baked.setInput(0, parentNode)
        tab = nuke.Tab_Knob('plus', 'plus')
        switcher = nuke.Enumeration_Knob('switcher', 'Matrix Type', ['All', 'Scale Only', 'Rotation Only', 'Translate Only', 'ScaleAndRotate Only'])
        finalMatrixArr = nuke.Array_Knob('finalMatrixKnob', 'All', 16)
        mtxScaleArr = nuke.Array_Knob('mtxScaleKnob', 'Scale Only', 16)
        mtxRotationArr = nuke.Array_Knob('mtxRotationKnob', 'Rotation Only', 16)
        mtxTranslationArr = nuke.Array_Knob('mtxTranslationKnob', 'Translate Only', 16)
        mtxScaleRotationArr = nuke.Array_Knob('mtxScaleRotationKnob', 'ScaleAndRotate Only', 16)
        #ADDING KNOBS
        check = node.knob('plus')
        if check is not None:
            baked.addKnob(switcher)
            for each in (finalMatrixArr, mtxScaleArr, mtxRotationArr,  mtxTranslationArr, mtxScaleRotationArr):
                baked.addKnob(each)
                each.setVisible(False)
        else:
            baked.addKnob(tab)
            baked.addKnob(switcher)
            for each in (finalMatrixArr, mtxScaleArr, mtxRotationArr,  mtxTranslationArr, mtxScaleRotationArr):
                baked.addKnob(each)
                each.setVisible(False)
        
        #FRAME RANGE
        range = nuke.getFramesAndViews('Get Frame Range',  '%s-%s' %(nuke.root().firstFrame(), nuke.root().lastFrame()) )
        frange = nuke.FrameRange(range[0])
        
        for n in frange:
            #GETTING KNOBS VALUES
            vectorsTo = [nuke.math.Vector2(node[f].getValueAt(n)[0], node[f].getValueAt(n)[1]) for f in sorted(node.knobs().keys()) if f.startswith('to')]
            vectorsFrom = [nuke.math.Vector2(node[f].getValueAt(n)[0], node[f].getValueAt(n)[1]) for f in sorted(node.knobs().keys()) if f.startswith('from')]
            
            #CONVERTING CORNER PIN TO MATRICES
            cornerPinMatrixTo.mapUnitSquareToQuad(vectorsTo[0].x, vectorsTo[0].y, vectorsTo[1].x, vectorsTo[1].y, vectorsTo[2].x, vectorsTo[2].y, vectorsTo[3].x, vectorsTo[3].y)
            cornerPinMatrixFrom.mapUnitSquareToQuad(vectorsFrom[0].x, vectorsFrom[0].y, vectorsFrom[1].x, vectorsFrom[1].y, vectorsFrom[2].x, vectorsFrom[2].y, vectorsFrom[3].x, vectorsFrom[3].y)
            
            #FINAL MATRIX VALUE
            finalMatrix = cornerPinMatrixTo * cornerPinMatrixFrom.inverse()
            finalMatrix.transpose()
        
            #DERIVATIVES
            mtxRotation = nuke.math.Matrix4(finalMatrix)
            mtxRotation.rotationOnly()
            mtxScale = nuke.math.Matrix4(finalMatrix)
            mtxScale.scaleOnly()
            mtxTranslation = nuke.math.Matrix4(finalMatrix)
            mtxTranslation.translationOnly()
            mtxScaleRotation = nuke.math.Matrix4(finalMatrix)
            mtxScaleRotation.scaleAndRotationOnly()
            #SET ANIMATED
            baked['finalMatrixKnob'].setAnimated()
            baked['mtxScaleKnob'].setAnimated()
            baked['mtxRotationKnob'].setAnimated()
            baked['mtxTranslationKnob'].setAnimated()
            baked['mtxScaleRotationKnob'].setAnimated()
        
            #ASSIGNING MATRICES TO KNOBS
            knobsCount = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
            
            [(baked['finalMatrixKnob'].setValueAt(finalMatrix[i], n, i)) for i in knobsCount]
            [(baked['mtxScaleKnob'].setValueAt(mtxScale[i], n, i)) for i in knobsCount]
            [(baked['mtxRotationKnob'].setValueAt(mtxRotation[i], n, i)) for i in knobsCount]
            [(baked['mtxTranslationKnob'].setValueAt(mtxTranslation[i], n, i)) for i in knobsCount]
            [(baked['mtxScaleRotationKnob'].setValueAt(mtxScaleRotation[i], n, i)) for i in knobsCount]
        
        baked['transform_matrix'].setExpression('finalMatrixKnob')
        print finalMatrix



####################################################################################
####################################################################################
# Matrix to CornerPin

def Matrix_to_CP():
    #DEFINING VARIABLES
    node = nuke.thisNode()
    knob = node.knob('transform_matrix')
    imageWidth = float(node.width())
    imageHeight = float(node.height())
    xps = node['xpos'].value()
    yps = node['ypos'].value()
    parent = node.input(0)
    sourceMatrix = nuke.math.Matrix4()
    
    #FRAME RANGE
    timerange = nuke.getFramesAndViews('Get Frame Range',  '%s-%s' %(nuke.root().firstFrame(), nuke.root().lastFrame()) )
    frange = nuke.FrameRange(timerange[0])
    
    #CREATING FROM MATRIX (IDENTITY MATRIX * IMAGE SIZE) 
    cpFrom = nuke.math.Matrix4()
    cpFrom.mapUnitSquareToQuad(0, 0, imageWidth, 0, imageWidth, imageHeight, 0, imageHeight)
    
    #CREATING TO VECTOR BEFORE APPLYING MATRIX
    vectorTo1 = nuke.math.Vector4(0,0,0,1)
    vectorTo2 = nuke.math.Vector4(1,0,0,1)
    vectorTo3 = nuke.math.Vector4(1,1,0,1)
    vectorTo4 = nuke.math.Vector4(0,1,0,1)
    
    #CREATING CORNERPIN NODE 
    cpFromMatrix = nuke.nodes.CornerPin2D(name=node.name()+'_fromMatrix', xpos=xps+100, ypos=yps)
    cpFromMatrix.setInput(0, parent)
    
    [cpFromMatrix[f].setAnimated() for f in sorted(node.knobs().keys()) if f.startswith('to')]
    
    for i in frange:
        knobValue = knob.valueAt(i)
        for each in range(0,16):
            sourceMatrix[each]=knobValue[each]
        
        sourceMatrix.transpose()
        finalMatrix = sourceMatrix * cpFrom
    
    
        transformedvectorTo1 = finalMatrix.transform(vectorTo1)
        to1 = ((transformedvectorTo1.x/transformedvectorTo1.w), (transformedvectorTo1.y/transformedvectorTo1.w))
        transformedvectorTo2 = finalMatrix.transform(vectorTo2)
        to2 = ((transformedvectorTo2.x/transformedvectorTo2.w), (transformedvectorTo2.y/transformedvectorTo2.w))
        transformedvectorTo3 = finalMatrix.transform(vectorTo3)
        to3 = ((transformedvectorTo3.x/transformedvectorTo3.w), (transformedvectorTo3.y/transformedvectorTo3.w))
        transformedvectorTo4 = finalMatrix.transform(vectorTo4)
        to4 = ((transformedvectorTo4.x/transformedvectorTo4.w), (transformedvectorTo4.y/transformedvectorTo4.w))
        print "\nto1 = ",to1,"\nto2 = ",to2,"\nto3 = ",to3,"\nto4 = ",to4
    
        for x in (0,1):
            cpFromMatrix['to1'].setValueAt(to1[x],i, x)
            cpFromMatrix['to2'].setValueAt(to2[x],i, x)
            cpFromMatrix['to3'].setValueAt(to3[x],i, x)
            cpFromMatrix['to4'].setValueAt(to4[x],i, x)
    
        cpFromMatrix['from2'].setValueAt(imageWidth,i,0)
        cpFromMatrix['from3'].setValueAt(imageWidth,i,0)
        cpFromMatrix['from3'].setValueAt(imageHeight,i,1)
        cpFromMatrix['from4'].setValueAt(imageHeight,i,1)


####################################################################################
####################################################################################

def Matrix_to_CP_toolbar():
    #DEFINING VARIABLES
    node = nuke.selectedNode()
    if node.Class() != 'CornerPin2D':
        nuke.message("please select a cornerpin node")
    else:
        knob = node.knob('transform_matrix')
        imageWidth = float(node.width())
        imageHeight = float(node.height())
        xps = node['xpos'].value()
        yps = node['ypos'].value()
        parent = node.input(0)
        sourceMatrix = nuke.math.Matrix4()
        
        #FRAME RANGE
        timerange = nuke.getFramesAndViews('Get Frame Range',  '%s-%s' %(nuke.root().firstFrame(), nuke.root().lastFrame()) )
        frange = nuke.FrameRange(timerange[0])
        
        #CREATING FROM MATRIX (IDENTITY MATRIX * IMAGE SIZE) 
        cpFrom = nuke.math.Matrix4()
        cpFrom.mapUnitSquareToQuad(0, 0, imageWidth, 0, imageWidth, imageHeight, 0, imageHeight)
        
        #CREATING TO VECTOR BEFORE APPLYING MATRIX
        vectorTo1 = nuke.math.Vector4(0,0,0,1)
        vectorTo2 = nuke.math.Vector4(1,0,0,1)
        vectorTo3 = nuke.math.Vector4(1,1,0,1)
        vectorTo4 = nuke.math.Vector4(0,1,0,1)
        
        #CREATING CORNERPIN NODE 
        cpFromMatrix = nuke.nodes.CornerPin2D(name=node.name()+'_fromMatrix', xpos=xps+100, ypos=yps)
        cpFromMatrix.setInput(0, parent)
        
        [cpFromMatrix[f].setAnimated() for f in sorted(node.knobs().keys()) if f.startswith('to')]
        
        for i in frange:
            knobValue = knob.valueAt(i)
            for each in range(0,16):
                sourceMatrix[each]=knobValue[each]
            
            sourceMatrix.transpose()
            finalMatrix = sourceMatrix * cpFrom
        
        
            transformedvectorTo1 = finalMatrix.transform(vectorTo1)
            to1 = ((transformedvectorTo1.x/transformedvectorTo1.w), (transformedvectorTo1.y/transformedvectorTo1.w))
            transformedvectorTo2 = finalMatrix.transform(vectorTo2)
            to2 = ((transformedvectorTo2.x/transformedvectorTo2.w), (transformedvectorTo2.y/transformedvectorTo2.w))
            transformedvectorTo3 = finalMatrix.transform(vectorTo3)
            to3 = ((transformedvectorTo3.x/transformedvectorTo3.w), (transformedvectorTo3.y/transformedvectorTo3.w))
            transformedvectorTo4 = finalMatrix.transform(vectorTo4)
            to4 = ((transformedvectorTo4.x/transformedvectorTo4.w), (transformedvectorTo4.y/transformedvectorTo4.w))
            print "\nto1 = ",to1,"\nto2 = ",to2,"\nto3 = ",to3,"\nto4 = ",to4
        
            for x in (0,1):
                cpFromMatrix['to1'].setValueAt(to1[x],i, x)
                cpFromMatrix['to2'].setValueAt(to2[x],i, x)
                cpFromMatrix['to3'].setValueAt(to3[x],i, x)
                cpFromMatrix['to4'].setValueAt(to4[x],i, x)
        
            cpFromMatrix['from2'].setValueAt(imageWidth,i,0)
            cpFromMatrix['from3'].setValueAt(imageWidth,i,0)
            cpFromMatrix['from3'].setValueAt(imageHeight,i,1)
            cpFromMatrix['from4'].setValueAt(imageHeight,i,1)


####################################################################################
####################################################################################
#CornerPin button (copy current 'to')

def copyCurrent():
    #copy to 'current'
    node = nuke.thisNode()
    knob1 = node['to1']
    knob2 = node['to2']
    knob3 = node['to3']
    knob4 = node['to4']
    knob5 = node['from1']
    knob6 = node['from2']
    knob7 = node['from3']
    knob8 = node['from4']
    list = []
    for each in [knob1, knob2, knob3, knob4]:
        list.append(each.value())
    x = 0
    for each in [knob5, knob6, knob7, knob8]:
        each.setValue(list[x])
        x += 1
        
        
####################################################################################







