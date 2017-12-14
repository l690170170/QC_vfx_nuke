import nuke
import os
import sys

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
