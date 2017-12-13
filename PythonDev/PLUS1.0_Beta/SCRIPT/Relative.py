import nuke

####################################################################################
#relative

def make_relative():
    PD = nuke.Root().knob("project_directory").value() 
    
    def relative():
        This = nuke.thisNode()
        sourceFile = This['file'].getValue()
        tempPath = sourceFile.split(PD)
        readname = tempPath[-1]
        fn = readname.split('./')
        print fn
        This['file'].setValue('./' + fn[-1])
    
    if not PD:
        nuke.message('Empty Project Directory in Project Settings')
    else:
        relative()
        print PD
####################################################################################
#relative from toolbar

def make_relative_Toolbar():
    PD = nuke.Root().knob("project_directory").value() 
    This = nuke.selectedNodes()
    if not PD:
        nuke.message('Empty Project Directory in Project Settings')
    else:
        for each in This:
            if each.Class() in ('Read', 'ReadGeo2'):
                def relative():
                    sourceFile = each['file'].getValue()
                    tempPath = sourceFile.split(PD)
                    readname = tempPath[-1]
                    fn = readname.split('./')
                    print fn
                    each['file'].setValue('./' + fn[-1])
                relative()
            else:
                 pass

####################################################################################     
#obsolute

def make_obsolute():
    PD = nuke.Root().knob("project_directory").value() 
    
    def obsolute():
        This = nuke.thisNode()
        sourceFile = This['file'].getValue()
        tempPath = sourceFile.split('./')
        readname = tempPath[-1]
        fn = readname.split(PD)
        This['file'].setValue(PD + fn[-1])
    
    
    if not PD:
        nuke.message('Empty Project Directory in Project Settings')
    else:
        obsolute()
        print PD

  
####################################################################################
#obsolute from toolbar

def make_obsolute_Toolbar():
    PD = nuke.Root().knob("project_directory").value()
    This = nuke.selectedNodes()
    if not PD:
        nuke.message('Empty Project Directory in Project Settings')
    else:
        for each in This:
            if each.Class() in ('Read', 'ReadGeo2'):
                def obsolute():
                    sourceFile = each['file'].getValue()
                    tempPath = sourceFile.split('./')
                    readname = tempPath[-1]
                    fn = readname.split(PD)
                    each['file'].setValue(PD + fn[-1])
                obsolute()
            else:
                pass

####################################################################################