import nuke
import nukescripts

####################################################################################
#RELOAD ALL READ NODES
def reloadReads():
    if not nuke.selectedNodes():
        mynodes = nuke.allNodes()
    else:  
        mynodes = nuke.selectedNodes()
    [ each.knob('reload').execute() for each in mynodes if each.Class() == 'Read' ]
    


####################################################################################
#MULTIPLE READ PANEL
    
class multiplereads( nukescripts.PythonPanel ):
    def __init__( self, node ):
        nukescripts.PythonPanel.__init__( self, 'Multiple Reads' )


        #Creating Knobs
        self.firstTab = nuke.Tab_Knob('Multiple Reads')
        self.first = nuke.Int_Knob( 'first', 'frame range' '')     
        self.before = nuke.Enumeration_Knob('before', '', ['hold', 'loop', 'bounce', 'black']) 
        self.before.clearFlag(nuke.STARTLINE)
        self.last = nuke.Int_Knob( 'last', '')
        self.last.clearFlag(nuke.STARTLINE)
        self.after = nuke.Enumeration_Knob('after', '', ['hold', 'loop', 'bounce', 'black']) 
        self.after.clearFlag(nuke.STARTLINE)

        self.frame_mode = nuke.Enumeration_Knob('frame', 'frame', ['exression', 'start at', 'offset']) 
        self.frame = nuke.String_Knob( 'frame', '' )  
        self.frame.clearFlag(nuke.STARTLINE)

        self.origfirst = nuke.Int_Knob( 'original range', 'origfirst' )      
        self.origlast = nuke.Int_Knob( 'origlast', '')     
        self.origlast.clearFlag(nuke.STARTLINE)

        self.on_error = nuke.Enumeration_Knob('on_error', 'on_error', ['error', 'black', 'checkerboard', 'nearest frame']) 

        self.colorspace = nuke.Enumeration_Knob('colorspace', 'colorspace', ['linear', 'sRGB',
                                                'rec709', 'Cineon', 'Gamma1.8', 'Gamma2.2', 'Gamma2.4', 'Panalog',
                                                'REDLog', 'ViperLog', 'AlexaV3LogC', 'PLogLin', 'SLog', 'SLog1',
                                                'SLog2', 'SLog3', 'CLog', 'Protune', 'REDSpace']) 
        self.premultiplied = nuke.Boolean_Knob('premultiplied', 'premultiplied')
        self.origlast.clearFlag(nuke.STARTLINE)
        self.raw = nuke.Boolean_Knob('raw', 'raw data')
        self.raw.clearFlag(nuke.STARTLINE)
        self.auto_alpha = nuke.Boolean_Knob('aalpha', 'auto alpha')
        self.auto_alpha.clearFlag(nuke.STARTLINE)
        
        #create Knobs
        self.tab = nuke.Tab_Knob("Affect only", None, nuke.TABBEGINCLOSEDGROUP)
        self.ALL = nuke.Boolean_Knob('ALL', 'All', 1)           
        self.firstE = nuke.Boolean_Knob('firstE', 'first', 1)
        self.firstE.setFlag(nuke.STARTLINE)
        self.firstE.setFlag(nuke.DISABLED)
        self.beforeE = nuke.Boolean_Knob('beforeE', 'before', 1)
        self.beforeE.setFlag(nuke.STARTLINE)
        self.beforeE.setFlag(nuke.DISABLED)
        self.lastE = nuke.Boolean_Knob('lastE', 'last', 1)
        self.lastE.setFlag(nuke.STARTLINE)
        self.lastE.setFlag(nuke.DISABLED)
        self.afterE = nuke.Boolean_Knob('afterE', 'after', 1)
        self.afterE.setFlag(nuke.STARTLINE)
        self.afterE.setFlag(nuke.DISABLED)
        self.frame_modeE = nuke.Boolean_Knob('frame_modeE', 'frame_mode', 1)
        self.frame_modeE.setFlag(nuke.STARTLINE)
        self.frame_modeE.setFlag(nuke.DISABLED)
        self.frameE = nuke.Boolean_Knob('frameE', 'frame', 1)
        self.frameE.setFlag(nuke.STARTLINE)
        self.frameE.setFlag(nuke.DISABLED)
        self.origfirstE = nuke.Boolean_Knob('origfirstE', 'origfirst', 1)
        self.origfirstE.setFlag(nuke.STARTLINE)
        self.origfirstE.setFlag(nuke.DISABLED)
        self.origlastE = nuke.Boolean_Knob('origlastE', 'origlast', 1)
        self.origlastE.setFlag(nuke.STARTLINE)
        self.origlastE.setFlag(nuke.DISABLED)
        self.on_errorE = nuke.Boolean_Knob('on_errorE', 'on_error', 1)
        self.on_errorE.setFlag(nuke.STARTLINE)
        self.on_errorE.setFlag(nuke.DISABLED)
        self.colorspaceE = nuke.Boolean_Knob('color_spaceE', 'color_space', 1)
        self.colorspaceE.setFlag(nuke.STARTLINE)
        self.colorspaceE.setFlag(nuke.DISABLED)
        self.premultipliedE = nuke.Boolean_Knob('premultipliedE', 'premultiplied', 1)
        self.premultipliedE.setFlag(nuke.STARTLINE)
        self.premultipliedE.setFlag(nuke.DISABLED)
        self.rawE = nuke.Boolean_Knob('rawE', 'raw', 1)
        self.rawE.setFlag(nuke.STARTLINE)
        self.rawE.setFlag(nuke.DISABLED)
        self.auto_alphaE = nuke.Boolean_Knob('auto_alphaE', 'auto_alpha', 1)
        self.auto_alphaE.setFlag(nuke.STARTLINE)
        self.auto_alphaE.setFlag(nuke.DISABLED)
        self.end = nuke.Tab_Knob("", None, nuke.TABENDGROUP) 


        #set initial values
        self.first.setValue(int(nuke.Root()['first_frame'].value()))
        self.origfirst.setValue(int(nuke.Root()['first_frame'].value()))
        self.last.setValue(int(nuke.Root()['last_frame'].value()))
        self.origlast.setValue(int(nuke.Root()['last_frame'].value()))

        #Adding knobs
        for k in ( self.firstTab, self.first, self.before, self.last, self.after, self.frame_mode,
                    self.frame, self.origfirst, self.origlast, self.on_error, self.colorspace,
                    self.premultiplied, self.raw, self.auto_alpha, self.tab, self.ALL, self.firstE,
                    self.beforeE, self.lastE, self.afterE, self.frame_modeE, self.frameE, self.origfirstE,
                    self.origlastE, self.on_errorE, self.colorspaceE, self.premultipliedE, self.rawE,
                    self.auto_alphaE, self.end ):
            self.addKnob( k )

        
    def knobChanged(self, knob):
        if knob in [self.ALL]:
            if self.ALL.value() == 1:
                for k in ( self.firstE, self.beforeE, self.lastE, self.afterE, self.frame_modeE,
                            self.frameE, self.origfirstE, self.origlastE, self.on_errorE, self.colorspaceE,
                            self.premultipliedE, self.rawE, self.auto_alphaE):
                    k.setFlag(nuke.DISABLED)
                    k.setValue(1)
            else :
                for k in ( self.firstE, self.beforeE, self.lastE, self.afterE, self.frame_modeE,
                            self.frameE, self.origfirstE, self.origlastE, self.on_errorE, self.colorspaceE,
                            self.premultipliedE, self.rawE, self.auto_alphaE ):
                    k.clearFlag(nuke.DISABLED)
                    k.setValue(0)

def showMulReads():

    #Showing the window
    panel = multiplereads(nuke.allNodes('Read'))
    result = panel.showModalDialog()
    #Printing the result
    if result == 1:
        #Specifing Target Nodes
        if not nuke.selectedNodes('Read'):
            target = nuke.allNodes('Read')
        else:  
            target = nuke.selectedNodes('Read')
        print("executing")
        [ each.knob('first').setValue(int(panel.first.value())) for each in target if panel.firstE.value() == 1 ]
        [ each.knob('before').setValue(panel.before.value()) for each in nuke.allNodes('Read') if panel.beforeE.value() == 1 ]
        [ each.knob('last').setValue(int(panel.last.value())) for each in nuke.allNodes('Read') if panel.lastE.value() == 1 ]
        [ each.knob('after').setValue(panel.after.value()) for each in nuke.allNodes('Read') if panel.afterE.value() == 1 ]
        [ each.knob('frame_mode').setValue(panel.frame_mode.value()) for each in nuke.allNodes('Read') if panel.frame_modeE.value() == 1 ]
        [ each.knob('frame').setValue(panel.frame.value()) for each in nuke.allNodes('Read') if panel.frameE.value() == 1 ]
        [ each.knob('origfirst').setValue(int(panel.origfirst.value())) for each in nuke.allNodes('Read') if panel.origfirstE.value() == 1 ]
        [ each.knob('origlast').setValue(int(panel.origlast.value())) for each in nuke.allNodes('Read') if panel.origlastE.value() == 1 ]
        [ each.knob('on_error').setValue(panel.on_error.value()) for each in nuke.allNodes('Read') if panel.on_errorE.value() == 1 ]
        [ each.knob('colorspace').setValue(panel.colorspace.value()) for each in nuke.allNodes('Read') if panel.colorspaceE.value() == 1 ]
        [ each.knob('premultiplied').setValue(panel.premultiplied.value()) for each in nuke.allNodes('Read') if panel.premultipliedE.value() == 1 ]
        [ each.knob('raw').setValue(panel.raw.value()) for each in nuke.allNodes('Read') if panel.rawE.value() == 1 ]
        [ each.knob('auto_alpha').setValue(panel.auto_alpha.value()) for each in nuke.allNodes('Read') if panel.auto_alphaE.value() == 1 ]
    else:
        print("Canceled")






####################################################################################
#MULTIPLE NODES PANEL

class multiplenodes( nukescripts.PythonPanel ):
    def __init__( self, node ):
        nukescripts.PythonPanel.__init__( self, 'Multiple Nodes' )


        #Creating Knobs
        self.name = nuke.String_Knob( 'name', 'Knob name' ) 
        self.enum = nuke.Enumeration_Knob('enum', 'Knob Type', ['integer', 'slider', 'double',
                                          'XY', 'XYZ', 'rgb', 'rgba', 'bbox', 'string', 'boolean'])
        self.enum.setFlag(nuke.STARTLINE)

        self.boolean = nuke.Boolean_Knob('boolean', 'boolean')
        self.boolean.setFlag(nuke.STARTLINE)
        self.boolean.setFlag(nuke.INVISIBLE)

        self.integer = nuke.Int_Knob( 'integer', 'integer' '')    
        self.integer.setFlag(nuke.STARTLINE) 
        self.integer.setFlag(nuke.INVISIBLE)

        self.slider = nuke.Double_Knob( 'slider', 'slider'  )  
        self.slider.setFlag(nuke.STARTLINE)

        self.double = nuke.WH_Knob( 'double', 'double'  )  
        self.double.setFlag(nuke.STARTLINE)
        self.double.setFlag(nuke.INVISIBLE)

        self.XY = nuke.UV_Knob( 'XY', 'XY'  )  
        self.XY.setFlag(nuke.STARTLINE)
        self.XY.setFlag(nuke.INVISIBLE)

        self.XYZ = nuke.Scale_Knob( 'XYZ', 'XYZ'  )  
        self.XYZ.setFlag(nuke.STARTLINE)
        self.XYZ.setFlag(nuke.INVISIBLE)

        self.rgb = nuke.Color_Knob( 'rgb', 'rgb' )  
        self.rgb.setFlag(nuke.STARTLINE)
        self.rgb.setFlag(nuke.INVISIBLE)

        self.rgba = nuke.AColor_Knob( 'rgba', 'rgba' )  
        self.rgba.setFlag(nuke.STARTLINE)
        self.rgba.setFlag(nuke.INVISIBLE)

        self.bbox = nuke.BBox_Knob( 'bbox', 'bbox' )  
        self.bbox.setFlag(nuke.STARTLINE)
        self.bbox.setFlag(nuke.INVISIBLE)

        self.string = nuke.String_Knob( 'string', 'string' )  
        self.string.setFlag(nuke.STARTLINE)
        self.string.setFlag(nuke.INVISIBLE)




        

        #set initial values
        self.enum.setValue('slider')


        #Adding knobs
        for k in (  self.name, self.enum, self.integer, self.slider, self.double, self.XY,
                    self.XYZ, self.rgb, self.rgba, self.bbox, self.string, self.boolean ):
            self.addKnob( k )

   
    def knobChanged(self, knob):
        if knob in [self.enum]:
            if self.enum.value() == 'integer':
                for k in ( self.integer, self.slider, self.double, self.XY, self.XYZ, self.rgb,
                            self.rgba, self.bbox, self.string, self.boolean):
                    k.setFlag(nuke.INVISIBLE)
                self.integer.clearFlag(nuke.INVISIBLE)
            if self.enum.value() == 'slider':
                for k in ( self.integer, self.slider, self.double, self.XY, self.XYZ, self.rgb,
                            self.rgba, self.bbox, self.string, self.boolean):
                    k.setFlag(nuke.INVISIBLE)
                self.slider.clearFlag(nuke.INVISIBLE)
            if self.enum.value() == 'double':
                for k in ( self.integer, self.slider, self.double, self.XY, self.XYZ, self.rgb,
                            self.rgba, self.bbox, self.string, self.boolean):
                    k.setFlag(nuke.INVISIBLE)
                self.double.clearFlag(nuke.INVISIBLE)
            if self.enum.value() == 'XY':
                for k in ( self.integer, self.slider, self.double, self.XY, self.XYZ, self.rgb,
                            self.rgba, self.bbox, self.string, self.boolean):
                    k.setFlag(nuke.INVISIBLE)
                self.XY.clearFlag(nuke.INVISIBLE)
            if self.enum.value() == 'XYZ':
                for k in ( self.integer, self.slider, self.double, self.XY, self.XYZ, self.rgb,
                            self.rgba, self.bbox, self.string, self.boolean):
                    k.setFlag(nuke.INVISIBLE)
                self.XYZ.clearFlag(nuke.INVISIBLE)
            if self.enum.value() == 'rgb':
                for k in ( self.integer, self.slider, self.double, self.XY, self.XYZ, self.rgb,
                            self.rgba, self.bbox, self.string, self.boolean):
                    k.setFlag(nuke.INVISIBLE)
                self.rgb.clearFlag(nuke.INVISIBLE)
            if self.enum.value() == 'rgba':
                for k in ( self.integer, self.slider, self.double, self.XY, self.XYZ, self.rgb,
                            self.rgba, self.bbox, self.string, self.boolean):
                    k.setFlag(nuke.INVISIBLE)
                self.rgba.clearFlag(nuke.INVISIBLE)
            if self.enum.value() == 'bbox':
                for k in ( self.integer, self.slider, self.double, self.XY, self.XYZ, self.rgb,
                            self.rgba, self.bbox, self.string, self.boolean):
                    k.setFlag(nuke.INVISIBLE)
                self.bbox.clearFlag(nuke.INVISIBLE)
            if self.enum.value() == 'string':
                for k in ( self.integer, self.slider, self.double, self.XY, self.XYZ, self.rgb,
                            self.rgba, self.bbox, self.string, self.boolean):
                    k.setFlag(nuke.INVISIBLE)
                self.string.clearFlag(nuke.INVISIBLE)
            if self.enum.value() == 'boolean':
                for k in ( self.integer, self.slider, self.double, self.XY, self.XYZ, self.rgb,
                            self.rgba, self.bbox, self.string, self.boolean):
                    k.setFlag(nuke.INVISIBLE)
                self.boolean.clearFlag(nuke.INVISIBLE)

#( self.integer, self.slider, self.double, self.XY, self.XYZ, self.rgb, self.rgba, self.bbox, self.string, self.boolean)


def showMulNodes():

    #Printing the result
    if not nuke.selectedNodes():
        nuke.message('Please select some nodes')
        pass
    else:
        #CHECK FOR SIMILAR CLASSES
        myClass = nuke.selectedNode().Class()
        for each in nuke.selectedNodes():
            if each.Class() != myClass :
                classresult = 0
            else:
                classresult = 1
        
        if classresult == 0:
            nuke.message('Please select similar nodes')
        else:
            #Showing the window
            panel = multiplenodes(nuke.allNodes('Read'))
            result = panel.showModalDialog()
            if result == 1:
                target = nuke.selectedNodes()
                #myClass = nuke.selectedNode().Class()
        
                    
                print(panel.name.value())
            
                if panel.enum.value() == 'integer':
                    for each in target:
                        each[panel.name.value()].setValue(panel.integer.value())               
                elif panel.enum.value() == 'slider':
                    for each in target:
                        each[panel.name.value()].setValue(panel.slider.value())   
                elif panel.enum.value() == 'double':
                    for each in target:
                        each[panel.name.value()].setValue(panel.double.value()) 
                elif panel.enum.value() == 'XY':
                    for each in target:
                        each[panel.name.value()].setValue(panel.XY.value()) 
                elif panel.enum.value() == 'XYZ':
                    for each in target:
                        each[panel.name.value()].setValue(panel.XYZ.value()) 
                elif panel.enum.value() == 'rgb':
                    for each in target:
                        each[panel.name.value()].setValue(panel.rgb.value()) 
                elif panel.enum.value() == 'rgba':
                    for each in target:
                        each[panel.name.value()].setValue(panel.rgba.value()) 
                elif panel.enum.value() == 'bbox':
                    for each in target:
                        each[panel.name.value()].setValue(panel.intebboxger.value()) 
                elif panel.enum.value() == 'string':
                    for each in target:
                        each[panel.name.value()].setValue(panel.string.value()) 
                elif panel.enum.value() == 'boolean':
                    for each in target:
                        each[panel.name.value()].setValue(panel.boolean.value()) 
            
            else:
                print("Canceled")