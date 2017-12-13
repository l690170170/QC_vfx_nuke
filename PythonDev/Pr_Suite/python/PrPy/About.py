"""
Script Name: About
Version: 1.1
Purpose: Pr_Suite About
Created For: Pr_Suite v1.1
Created On: 10/06/2016
Author: Parimal Desai
Website: www.parimalvfx.com
History:
v1.0 (01/10/2015)
    Pr_Suite About
v1.1 (10/06/2016)
    Added Pr_Suite documentation.
    PEP 8 compliant.
"""

import os
import webbrowser
import nuke
import nukescripts


def docs():
    """
    Pr_Suite Documentation
    """
    doc = False
    for search in nuke.pluginPath():
        docPath = os.path.dirname(search) + "/documentation/Pr_Suite v1.1 Documentation.html"
        if os.path.exists(docPath):
            webbrowser.open("file:///" + docPath)
            doc = True
            break

    if doc is False:
        if nuke.ask(
                "Pr_Suite documentation not found in expected installation directory. Click on 'Yes' to access online "
                "Pr_Suite documentation."):
            webbrowser.open("http://bit.ly/PrSuiteDocumentation")


def about():
    """
    Pr_Suite About
    """
    class AboutPanel(nukescripts.PythonPanel):
        def __init__(self):
            nukescripts.PythonPanel.__init__(self, "About Pr_Suite", "com.parimalvfx.AboutPanel")
            self.setMinimumSize(311, 311)
            self.banner = nuke.PyScript_Knob("about", "<img src='About_Pr_Suite.png'>",
                                             "webbrowser.open('http://www.parimalvfx.com/rnd/pr_suite/')")
            self.addKnob(self.banner)

    launch = AboutPanel()
    launch.showModal()
