import nuke
import os
import sys
import subprocess

####################################################################################
# open nuke tmp path


def opentmp():
    def open(path):
        if os.path.exists( path ):
            if(sys.platform == 'win32'):
                os.system('start ' + path)
            elif(sys.platform == 'darwin'):
                os.system('open ' + path)
            else:
                subprocess.Popen(['xdg-open', path])
        else:
            nuke.message('Path is empty:\n' + path)
    open((os.environ['NUKE_TEMP_DIR']))


####################################################################################
# open nuke script path
def openScriptFolder():

    #GETTING SCRIPT PATH AND ADDING '/' AT THE END
    file = nuke.script_directory()
    splitList = file.split( '/' )
    path = ""
    for i in range(0, (len(splitList))):
        path += splitList[i] + '/'

    #WORK AROUND FOR WHITE SPACES IN STRING IF ANY
    spacespath=''
    spaceList = path.split( ' ' )
    for i in range(0, (len(spaceList))):
        spacespath += spaceList[i] + '\ '
    FinalPath=''
    spaceList2 = spacespath.split( '/' )
    spaceList2.pop(-1)
    FinalPath = '/'.join(spaceList2)+'/'
    print FinalPath

    #DOING THE WORK
    def open(path):
        if os.path.exists( file ):
            if(sys.platform == 'win32'):
                os.system('start ' + FinalPath)
            elif(sys.platform == 'darwin'):
                os.system('open ' + FinalPath)
            else:
                subprocess.Popen(['xdg-open', FinalPath])
        else:
            nuke.message('Path is empty:\n' + file)

    open(FinalPath)
    

####################################################################################
####################################################################################
# open nuke project_directory path
def openProjectFolder():

    #GETTING SCRIPT PATH AND ADDING '/' AT THE END
    file = nuke.root().knob("project_directory").value()
    print file

    #WORK AROUND FOR WHITE SPACES IN STRING IF ANY
    spacespath=''
    spaceList = file.split( ' ' )
    for i in range(0, (len(spaceList))):
        spacespath += spaceList[i] + '\ '
    print spacespath
    FinalPath=''
    spaceList2 = spacespath.split( '/' )
    spaceList2.pop(-1)
    FinalPath = '/'.join(spaceList2)+'/'
    print FinalPath

    #DOING THE WORK
    def open(path):
        if os.path.exists( file ):
            if(sys.platform == 'win32'):
                os.system('start ' + FinalPath)
            elif(sys.platform == 'darwin'):
                os.system('open ' + FinalPath)
            else:
                subprocess.Popen(['xdg-open', FinalPath])
        else:
            nuke.message('Path is empty:\n' + file)

    open(FinalPath)
    
    
####################################################################################
####################################################################################
#open read folder

def plusOpen():
    This = nuke.thisNode()
    
    file = This['file'].value()
    splitList = file.split( './' )
    joinedList = ''.join(splitList)
    if joinedList != file :
        projDir = nuke.root().knob("project_directory").value()
        absolutePath = projDir + joinedList
    else :
        absolutePath = file
    
    #REMOVING FILE NAME
    splitList = absolutePath.split( '/' )
    splitList.pop(-1)
    path = ""
    for i in range(0, (len(splitList))):
        path += splitList[i] + '/'
    
    #WORK AROUND FOR WHITE SPACES IN STRING IF ANY
    spacespath=''
    spaceList = path.split( ' ' )
    for i in range(0, (len(spaceList))):
        spacespath += spaceList[i] + '\ '
    FinalPath=''
    spaceList2 = spacespath.split( '/' )
    spaceList2.pop(-1)
    FinalPath = '/'.join(spaceList2)+'/'
    
    #EXECUTING
    if os.path.exists( path ):
        if(sys.platform == 'win32'):
            os.system('start ' + FinalPath)
        elif(sys.platform == 'darwin'):
            os.system('open ' + FinalPath)
        else:
            subprocess.Popen(['xdg-open', FinalPath])
    else:
        nuke.message('Path is empty:\n' + path)
  
####################################################################################
#open read folder from toolbar
def plusOpen_toolbar():
    This = nuke.selectedNodes()
    emptyList = []
    for each in This:
        try:
            file = each['file'].value()
            #ABSOLUTE PATH
            splitList = file.split( './' )
            joinedList = ''.join(splitList)
            if joinedList != file :
                projDir = nuke.root().knob("project_directory").value()
                absolutePath = projDir + joinedList
            else :
                absolutePath = file
            
            #REMOVING FILE NAME
            splitList = absolutePath.split( '/' )
            splitList.pop(-1)
            path = ""
            for i in range(0, (len(splitList))):
                path += splitList[i] + '/'
            
            #WORK AROUND FOR WHITE SPACES IN STRING IF ANY
            spacespath=''
            spaceList = path.split( ' ' )
            for i in range(0, (len(spaceList))):
                spacespath += spaceList[i] + '\ '
            FinalPath=''
            spaceList2 = spacespath.split( '/' )
            spaceList2.pop(-1)
            FinalPath = '/'.join(spaceList2)+'/'
            
            #EXECUTING
            if os.path.exists( path ):
                if(sys.platform == 'win32'):
                    os.system('start ' + FinalPath)
                elif(sys.platform == 'darwin'):
                    os.system('open ' + FinalPath)
                else:
                    subprocess.Popen(['xdg-open', FinalPath])
            else:
                emptyList.append(each.name())
        except:
            emptyList.append(each.name())
    emptyNodes = '\n'.join(emptyList)
    print ('File knob is either empty or non existant for:\n' + emptyNodes)


   
####################################################################################


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

