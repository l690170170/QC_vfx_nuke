import nuke, nukescripts

####################################################################################
#LOCK ALL KNOBS ON SELECTED NODES
def LockNodes():
    #LOCK NODES
    index = 0
    list = []
    while index < len(nuke.selectedNodes()):
        node = nuke.selectedNodes()[index]
        for each in node.allKnobs():
            list.append(each)
        print '\n', node.name()
        index = index+1
    
    for each in list:
        each.setEnabled(False)

####################################################################################
#UNLOCK ALL KNOBS ON SELECTED NODES
def UnlockNodes():
    #UNLOCK NODES
    index = 0
    list = []
    while index < len(nuke.selectedNodes()):
        node = nuke.selectedNodes()[index]
        for each in node.allKnobs():
            list.append(each)
        print '\n', node.name()
        index = index+1
    
    for each in list:
        each.setEnabled(True)

####################################################################################
#HIDE ALL KNOBS ON SELECTED NODES
def HideNodes():
    #LOCK NODES
    index = 0
    list = []
    while index < len(nuke.selectedNodes()):
        node = nuke.selectedNodes()[index]
        for each in node.allKnobs():
            list.append(each)
        print '\n', node.name()
        index = index+1
    
    for each in list:
        each.setVisible(False)

####################################################################################
#UNHIDE ALL KNOBS ON SELECTED NODES
def UnhideNodes():
    #UNLOCK NODES
    index = 0
    list = []
    while index < len(nuke.selectedNodes()):
        node = nuke.selectedNodes()[index]
        for each in node.allKnobs():
            list.append(each)
        print '\n', node.name()
        index = index+1
    
    for each in list:
        each.setVisible(True)
        
        
####################################################################################
#LOCK PANEL

def getSelected():
    try:
        node = nuke.selectedNode()
    except:
        nuke.message('No node selected')
    return node

def getList(node):
    list = []
    for each in getSelected().allKnobs():
        list.append(each.name())
    list2 = '\n'.join(list)
    return list2

class LockKnobs(nukescripts.PythonPanel):

    def __init__(self, node):
        nukescripts.PythonPanel.__init__(self, 'Lock Knobs')
        #CREATE KNOBS
        self.AllKnobs = nuke.PyScript_Knob('AllKnobs', 'All Knobs')
        self.Clear = nuke.PyScript_Knob('Clear', 'Clear')
        self.Knobslist = nuke.Multiline_Eval_String_Knob('Knobs', 'Knobs')
        self.Operation = nuke.Enumeration_Knob('Operation', 'Operation', ['Hide', 'Show', 'Lock', 'Unlock'])
        #ADD KNOBS
        for k in ( self.AllKnobs, self.Clear, self.Knobslist, self.Operation):
            self.addKnob(k)

    def knobChanged(self, knob):
        if knob is self.AllKnobs:
            self.Knobslist.setValue(getList(getSelected()))
        elif knob is self.Clear:
            self.Knobslist.setValue('')


    
def showLockPanel():  
    try:
        node = nuke.selectedNode()

        Lockpanel = LockKnobs(node)
        result = Lockpanel.showModalDialog() 
    
        x = []
        for each in Lockpanel.Knobslist.value():
            if each != '\n':
                x.append(each)
            if each == '\n':
                x.append('|')
        y = ''.join(x)
        z = y.split('|')
    
        if result == True:
            if Lockpanel.Operation.value() == 'Hide': 
                for each in z:
                    nuke.selectedNode()[each].setVisible(False)
            elif Lockpanel.Operation.value() == 'Show':
                for each in z:
                    nuke.selectedNode()[each].setVisible(True)
            elif Lockpanel.Operation.value() == 'Lock':
                for each in z:
                    nuke.selectedNode()[each].setEnabled(False)
            elif Lockpanel.Operation.value() == 'Unlock':
                for each in z:
                    nuke.selectedNode()[each].setEnabled(True)
        else:
            print 'Canceled'
    except:
        nuke.message('No node selected')
####################################################################################