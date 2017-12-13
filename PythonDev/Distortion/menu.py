toolbar = nuke.menu('Nodes')
m = toolbar.addMenu('litb_toolbar',icon="sxj.png")
m.addCommand('SyLens/SyCamra',"nuke.createNode('SyCamera')")
m.addCommand('SyLens/SyGeo',"nuke.createNode('SyGeo')")
m.addCommand('SyLens/SyLens',"nuke.createNode('SyLens')")
m.addCommand('SyLens/SyShader',"nuke.createNode('SyShader')")
m.addCommand('SyLens/SyUV',"nuke.createNode('SyUV')")
m.addCommand('SyLens/synth_template',"nuke.createNode('synth_template.nk')")
m.addCommand('SyLens',)
m.addCommand('3DE/LD_3DE_Classic_LD_Model',"nuke.createNode('LD_3DE_Classic_LD_Model')")
m.addCommand('3DE/LD_3DE4_All_Parameter_Types',"nuke.createNode('LD_3DE4_All_Parameter_Types')")
m.addCommand('3DE/LD_3DE4_Anamorphic_Degree_6',"nuke.createNode('LD_3DE4_Anamorphic_Degree_6')")
m.addCommand('3DE/LD_3DE4_Anamorphic_Standard_Degree_4',"nuke.createNode('LD_3DE4_Anamorphic_Standard_Degree_4')")
m.addCommand('3DE/LD_3DE4_Radial_Fisheye_Degree_8',"nuke.createNode('LD_3DE4_Radial_Fisheye_Degree_8')")
m.addCommand('3DE/LD_3DE4_Radial_Standard_Degree_4',"nuke.createNode('LD_3DE4_Radial_Standard_Degree_4')")
m.addCommand('3DE/LD_3DE_template',"nuke.createNode('LD_3DE_template.nk')")

m.addCommand('3DE',)




