# -*- coding: utf-8 -*-
# __author__ = 'XingHuan'
# 4/16/2017

import nuke
import toolSet

def add_pluginPath(pluginPathList):
    for pluginPath in pluginPathList:
        nuke.pluginAddPath(pluginPath)


def load_plugins(menu, categories):
    for category in categories:
        if category.split(".")[-1] in ["gizmo", "dll", "so"]:
            tempCategory = category.replace(".%s" % category.split(".")[-1], "")
            pluginName = tempCategory.split("/")[-1]
            menu.addCommand(tempCategory, "nuke.createNode('%s')" % pluginName, icon = "%s.png" % pluginName)
        elif category.split(".")[-1] == "nk":
            tempCategory = category.replace(".%s" % category.split(".")[-1], "")
            pluginName = tempCategory.split("/")[-1]
            menu.addCommand(tempCategory, "nuke.nodePaste('%s/%s')" % (toolSet.RootPath, category), icon = "%s.png" % pluginName)





toolbar = nuke.toolbar("Nodes")
toolSetMenu = toolbar.addMenu("BC_ToolSet", icon = "toolSet.png")

def refresh_plugins():
	toolSetMenu.clearMenu()
	toolSetMenu.addCommand("refresh", refresh_plugins)
	toolSetMenu.addCommand("add to toolset", "toolSet.add_toolset();refresh_plugins()")
	toolSetMenu.addSeparator()
	allPluginsList = toolSet.walk_dir(toolSet.RootPath)
	allPluginPathList = toolSet.get_pluginPath(allPluginsList)
	allCategory = toolSet.get_categories(allPluginsList)
	#print allCategory
	add_pluginPath(allPluginPathList)
	load_plugins(toolSetMenu, allCategory)


refresh_plugins()