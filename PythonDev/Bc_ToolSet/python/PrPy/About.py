"""
Script Name: About
Version: 1.1
Purpose: Bc_ToolSet About
Created For: Bc_ToolSet v1.1
Created On: 10/06/2016
Author: Parimal Desai
Website: www.parimalvfx.com
History:
v1.0 (01/10/2015)
    Bc_ToolSet About
v1.1 (10/06/2016)
    Added Bc_ToolSet documentation.
    PEP 8 compliant.
"""

import os
import webbrowser
import nuke
import nukescripts


def docs():
    """
    Bc_ToolSet Documentation
    """
    doc = False
    for search in nuke.pluginPath():
        docPath = os.path.dirname(search) + "/documentation/Bc_ToolSet v1.1 Documentation.html"
        if os.path.exists(docPath):
            webbrowser.open("file:///" + docPath)
            doc = True
            break

    if doc is False:
        if nuke.ask(
                "Bc_ToolSet documentation not found in expected installation directory. Click on 'Yes' to access online "
                "Bc_ToolSet documentation."):
            webbrowser.open("http://bit.ly/PrSuiteDocumentation")


def about():
    """
    Bc_ToolSet About
    """
    class AboutPanel(nukescripts.PythonPanel):
        def __init__(self):
            nukescripts.PythonPanel.__init__(self, "About Bc_ToolSet", "com.parimalvfx.AboutPanel")
            self.setMinimumSize(311, 311)
            self.banner = nuke.PyScript_Knob("about", "<img src='About_Bc_ToolSet.png'>",
                                             "webbrowser.open('http://www.parimalvfx.com/rnd/Bc_ToolSet/')")
            self.addKnob(self.banner)

    launch = AboutPanel()
    launch.showModal()
