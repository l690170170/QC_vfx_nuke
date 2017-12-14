"""
Script Name: OpenFolder
Version: 1.0
Purpose: Open folder based on user given path.
Created For: Pr_Suite v1.1
Created On: 08/05/2016
Author: Parimal Desai
Website: www.parimalvfx.com
History:
v1.0 (08/05/2016)
    First function to open folder based on OS.
    Rest all functions to open specific path.
"""

import platform
import os
import subprocess
import getpass
import nuke
import nukescripts


def open_folder(path):
    """
    Open folder based on OS.
    :param path: Directory path
    :type path: str
    :return: None
    :rtype: None
    """
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    elif platform.system() == "Linux":
        subprocess.check_call(["gnome-open", path])
    else:
        nuke.message("Unsupported OS")


def open_read_file():
    """
    Open folder for selected node with file knob.
    :return: None
    :rtype: None
    """
    read_path = nuke.selectedNode()["file"].value()
    open_folder(os.path.dirname(read_path))


def open_nuke_script():
    """
    Open folder for current saved Nuke script.
    :return: None
    :rtype: None
    """
    script_path = nuke.root()["name"].value()
    if not script_path == "":
        open_folder(os.path.dirname(script_path))
    else:
        nuke.message("Please save your Nuke script first.")


def open_dot_nuke():
    """
    Open .nuke folder.
    :return: None
    :rtype: None
    """
    current_user = getpass.getuser()
    if platform.system() == "Windows":
        open_folder("C:/Users/%s/.nuke" % current_user)
    elif platform.system() == "Darwin":
        open_folder("Users/%s/.nuke" % current_user)
    elif platform.system() == "Linux":
        open_folder("/home/%s/.nuke" % current_user)
    else:
        nuke.message("Unsupported OS")


def open_specific_plugin_path():
    """
    Open folder for selected path from Nuke's Plugin Paths.
    :return: None
    :rtype: None
    """
    class SpecificPathPanel(nukescripts.PythonPanel):
        def __init__(self):
            nukescripts.PythonPanel.__init__(self, "Open Specific Plugin Path Folder")
            paths = []
            plugin_path = nuke.pluginPath()
            for each in plugin_path:
                paths.append(os.path.normpath(each))
            self.ppaths = nuke.Enumeration_Knob("plugin_paths", "Select Path", paths)
            self.addKnob(self.ppaths)

        def knobChanged(self, knob):
            if knob.name() == "OK":
                try:
                    open_folder(self.ppaths.value())
                except:
                    nuke.message("Can't open folder for selected path.")

    show = SpecificPathPanel()
    show.showModalDialog()
