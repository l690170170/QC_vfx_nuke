import sys
import nuke
 
 
print 'Loading Lab Tools...'


import os.path
toolbar=nuke.menu("Nodes")

m=toolbar.addMenu("Blue Castle",icon="ff.png")


m.addCommand("showDirtyAlpha","nuke.createNode(\"showDirtyAlpha\")","showDirtyAlpha.png")


m.addCommand("Color_spill","nuke.createNode(\"Color_spill\")","#z","Color_spill.png")




m.addCommand("Litb_BGClear","nuke.createNode(\"Litb_BGClear\")","#b","Litb_BGClear.png")

m.addCommand("extrudeeedge","nuke.createNode(\"extrudeeedge.gizmo\")","testMenu.png")




m.addCommand("Despill","nuke.createNode(\"Despill\")","Despill.png")

m.addCommand("DespillMadness","nuke.createNode(\"DespillMadness\")","#w","testMenu.png")


m.addCommand("upscale","nuke.createNode(\"upscale\")","upscale.png")





m.addCommand("LumaDespill","nuke.createNode(\"LumaDespill\")","testMenu.png")


m.addCommand("CropMask","nuke.createNode(\"CropMask\")","testMenu.png")


m.addCommand("edgeDespill","nuke.createNode(\"edgeDespill\")",icon="tt.png")


m.addCommand("hairEasyKey","nuke.createNode(\"hairEasyKey\")","testMenu.png")


m.addCommand("EdgeEx","nuke.createNode(\"EdgeEx\")","testMenu.png")

m.addCommand("Deinterlacer","nuke.createNode(\"Deinterlacer\")","Deinterlacer.png")

m.addCommand("delivery_text", "nuke.createNode(\"delivery_text\")", icon="network.png")


#m.addCommand("Transform/CamQuake!", "nuke.createNode(\"CamQuake\")", icon="CamQuake.png")


m.addCommand("Day2Night", "nuke.createNode(\"Day2Night\")", icon="Day2Night.png")

m.addCommand("RainMaker", "nuke.createNode(\"RainMaker\")", icon="raining.png")

m.addCommand("switchMatte", "nuke.createNode(\"switchMatte\")", icon="masktchi.png")

m.addCommand("RealChromaticAberration", "nuke.createNode(\"RealChromaticAberration\")", icon="Chromatic_Ab_Icon.png")

m.addCommand("RealHeatDistortion", "nuke.createNode(\"RealHeatDistortion\")", icon="RealHeatDistortionIcon.png")

m.addCommand("RealHeatDistortion", "nuke.createNode(\"RealHeatDistortion\")", icon="RealHeatDistortionIcon.png")

m.addCommand("vector_module", "nuke.createNode(\"vector_module\")", icon="vector_module.png")

m.addCommand("RainMaker3", "nuke.createNode(\"RainMaker3\")", icon="RainMaker3.png")

m.addCommand("CWDefocus", "nuke.createNode(\"CWDefocus\")", icon="CWDefocus.png")

m.addCommand("SpotFlare", "nuke.createNode(\"SpotFlare\")", icon="SpotFlare.png")


m.addCommand("Information_Reduction","nuke.createNode(\"Information_Reduction\")","video.png")

m.addCommand("ASURA_Information","nuke.createNode(\"ASURA_Information\")","ASURA_Information.png")

m.addCommand("ASURA_delivery_text","nuke.createNode(\"ASURA_delivery_text\")","ASURA_delivery_text.png")




import nuke
import os

#Define the function to be executed by the command
#Defina a fun??o a ser executada pelo comando

def WriteAuto():
    #Create the variables 
    #Crie as variaveis necessarias
    FileFolder = "String"
    customPreset = None
    sep = '"'
    #Put your projects name in the list variable bellow
    #Coloque todos os seus projetos dentro da variavel abaixo como no exemplo
    presets = ['Herbst', 'Axis']
    #Create the panel that will pop up on the command execution
    #crie o painel a ser aberto quando o comando for executado
    p = nuke.Panel('Choose Project')
    p.addEnumerationPulldown('Project',' '.join(presets))
    
    #Define a variable with the selected option
    #defina uma variavel com uma das opcoes de projetos
    if p.show():
        customPreset = p.value('Project')
	
	#Write Presets
	
	#at this point you should customize the script by the necessities of your projects
	#nesse passo o script deve ser personalizado conforme sua organizacao de projeto
	
    if customPreset == 'Herbst':
        rootFile = nuke.toNode('Read1').knob('file').getValue()
        rootImgSrc = os.path.dirname(rootFile)
        rootSrc = os.path.dirname(rootImgSrc)
        rootIn = os.path.dirname(rootSrc)
        rootShot = os.path.dirname(rootIn)
        FileFolder = rootShot+'/out'
        try:
            os.stat(FileFolder)
        except:
            os.mkdir(FileFolder)
    
    #Write node creation with the file extension and path
    #criacao do write node ja com a extensao necessaria para o projeto  
    w = nuke.createNode('Write')
    count = 1
    while nuke.exists('AutoWrite' + str(count)):
        count += 1
    w.knob('name').setValue('AutoWrite' + str(count))
    w.knob('file').setValue(FileFolder + '/render%d.exr')
    
    




# add fxT menu
sideBar = nuke.menu('Nodes')
fxT = sideBar.addMenu('fxT', icon='fxT_menu.png')

# add fxT_disableNodes Gizmo to the fxT menu
fxT.addCommand('fxT_disableNodes', "nuke.createNode('fxT_disableNodes')", 'Alt+d', icon='fxT_disableNodes.png')







import nuke, nukescripts, sys, os, errno
from Directories import *
from TwoD import *



toolbar = nuke.toolbar ( "PLUS" )
Dir = toolbar.addMenu ( 'Directories', icon = 'admin.png' )
Dir.addCommand( 'Open Script Folder', "openScriptFolder()" ,'shift+j' , icon='Dscript.png')

Dir.addSeparator()
Dir.addCommand( 'Read from Write', "PlusRFWLink_toolbar()",'shift+e' ,  icon='Drfw.png')



Organize = toolbar.addMenu ( 'Organize', icon = 'Orga.png' )
Organize.addSeparator()
Organize.addCommand( 'Lock Panel', 'showLockPanel()' ,'shift+i' , icon = 'Olp.png')



