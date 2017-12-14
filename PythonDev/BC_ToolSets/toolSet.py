# -*- coding: utf-8 -*-
# __author__ = 'XingHuan'
# 4/16/2017

import os
import nuke
import nukescripts

#RootPath = os.path.expanduser('~').replace('\\','/') + '/.nuke/BC_ToolSet/Plugins'
#2017年11月29日17:24:54（更改路径）
RootPath = "//192.168.0.2/PythonDev/BC_ToolSets/Plugins"

PluginFormat = ["gizmo", "nk", "dll", "so"]
curVersion = "%s.%s" % (nuke.env ["NukeVersionMajor"], nuke.env ["NukeVersionMinor"])

def walk_dir(dir,topdown=True):
    pathList = []
    for root, dirs, files in os.walk(dir, topdown):
        for file in files:
            absPath = os.path.join(root, file).replace("\\", "/")
            #print absPath
            if absPath.split(".")[-1] in PluginFormat:
                pathList.append(absPath)
    return pathList

def get_pluginPath(pluginsList):
    pluginPathList = []
    for plugin in pluginsList:
        pluginPath = os.path.dirname(plugin)
        if pluginPath not in pluginPathList:
            pluginPathList.append(pluginPath)
    deleteId = []
    for i in range(0, len(pluginPathList)):
		if len(pluginPathList[i].split(RootPath)[1].split("/"))>1:
			if pluginPathList[i].split(RootPath)[1].split("/")[1] == "Version":
				if pluginPathList[i].split(RootPath)[1].split("/")[2] != curVersion:
					deleteId.append(i)
    deleteId.sort(reverse = True)
    for i in deleteId:
        pluginPathList.pop(i)
    return pluginPathList

def get_categories(pluginsList):
    categories = []
    for plugin in pluginsList:
        category = plugin.replace("%s/" % RootPath, "")
        if category not in categories:
            categories.append(category)
    deleteId = []
    for i in range(0, len(categories)):
        if categories[i].split("/")[0] == "Version":
            if categories[i].split("/")[1] != curVersion:
                deleteId.append(i)
    deleteId.sort(reverse = True)
    for i in deleteId:
        categories.pop(i)
    return categories


def get_categories_rel(pluginsList):
    categories = [""]
    for plugin in pluginsList:
        category = "/".join(plugin.replace("%s/" % RootPath, "").split("/")[:-1]) + "/"
        if category not in categories:
            categories.append(category)
    deleteId = []
    for i in range(0, len(categories)):
        if categories[i].split("/")[0] == "Version":
            if categories[i].split("/")[1] != curVersion:
                deleteId.append(i)
    deleteId.sort(reverse = True)
    for i in deleteId:
        categories.pop(i)
    return categories


class AddToolSetPanel(nukescripts.PythonPanel):
    def __init__(self):
        nukescripts.PythonPanel.__init__(self, "Add ToolSet")
        self.choosePathKnob = nuke.Enumeration_Knob("addTo", "Add To", [""])
        self.choosePathKnob.setValues([""])
        self.nameKnob = nuke.String_Knob("Name")
        self.axisKnob = nuke.Axis_Knob("")
        self.okButton = nuke.PyScript_Knob("Ok")
        self.cancelButton = nuke.PyScript_Knob("Cancel")

        for knob in [self.choosePathKnob, self.nameKnob, self.axisKnob, self.okButton, self.cancelButton]:
            self.addKnob(knob)

    def refreshPath(self, list):
        self.choosePathKnob.setValues(list)

    def addToTool(self):
        input = self.nameKnob.value()
        if input == "":
            pass
        elif input.split("/")[-1] == "":
            pass
        else:
            file = "%s/%s.nk" % (RootPath, input)
            print file
            filePath = os.path.dirname(file)
            if not os.path.exists(filePath):
                os.makedirs(filePath)
            nuke.nodeCopy(file)

    def knobChanged(self, knob):
        if knob == self.choosePathKnob:
            self.nameKnob.setText(self.choosePathKnob.value())
        if knob == self.okButton:
            self.addToTool()
        if knob == self.cancelButton:
            print 0


panel = AddToolSetPanel()

def add_toolset():
    allPluginsList = walk_dir(RootPath)
    allCategory_rel = get_categories_rel(allPluginsList)
    panel.refreshPath(allCategory_rel)
    panel.showModal()





