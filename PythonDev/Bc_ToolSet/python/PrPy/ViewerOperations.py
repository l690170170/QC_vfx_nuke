"""
Script Name: ViewerOperations
Version: 1.0
Purpose: Viewer specific operations.
Created For: Bc_ToolSet v1.1
Created On: 04/05/2016
Author: Parimal Desai
Website: www.parimalvfx.com
History:
v1.0 (04/05/2016)
    First function to find currently active Viewer.
    Rest functions to perform Viewer operations.
"""

import nuke


def active_viewer():
    """
    Find name of currently active Viewer.
    :return: Name of currently active Viewer.
    :rtype: str
    """
    viewer = nuke.activeViewer()
    viewer_name = viewer.node()["name"].value()
    return viewer_name


def set_rgba():
    """
    Set Viewer channels to RGBA.
    :return: None
    :rtype: None
    """
    nuke.toNode(active_viewer())["channels"].setValue("rgba")


def label_input_process():
    """
    Set input process node name as label.
    :return: None
    :rtype: None
    """
    label = nuke.toNode(active_viewer())["label"]
    label_value = "[value input_process_node]"
    if label.value() == label_value:
        label.setValue("")
    else:
        label.setValue(label_value)
