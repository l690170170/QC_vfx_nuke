"""
Script Name: BringDownViewer
Version: 1.0
Purpose: Set viewer(s) node position under selected node.
Created For: Bc_ToolSet v1.1
Created On: 05/05/2016
Author: Parimal Desai
Website: www.parimalvfx.com
History:
v1.0 (05/05/2016)
    Set viewer(s) node position under selected node.
"""

import nuke


def bring_down_viewer():
    """
    Set viewer(s) node position under selected node.
    :return: None
    :rtype: None
    """
    selected = nuke.selectedNode()
    dependent = selected.dependent()
    selected_x_pos = selected.xpos()
    selected_y_pos = selected.ypos()
    viewer_list = []

    for viewer in dependent:
        if viewer.Class() == "Viewer":
            viewer_list.append(viewer)
        else:
            pass

    if len(viewer_list) == 1:
        viewer_list[0].setXpos(selected_x_pos)
        viewer_list[0].setYpos(selected_y_pos + 75)
    elif len(viewer_list) > 1:
        viewer_list[0].setXpos(selected_x_pos)
        viewer_list[0].setYpos(selected_y_pos + 75)
        viewer_zero_x_pos = viewer_list[0].xpos()
        viewer_zero_y_pos = viewer_list[0].ypos()
        del viewer_list[0]
        for viewer in viewer_list:
            viewer_index = viewer_list.index(viewer)
            if viewer_index == 0:
                viewer.setXpos(viewer_zero_x_pos)
                viewer.setYpos(viewer_zero_y_pos + 25)
            else:
                last_viewer = viewer_index - 1
                last_viewer_x_pos = viewer_list[last_viewer].xpos()
                last_viewer_y_pos = viewer_list[last_viewer].ypos()
                viewer.setXpos(last_viewer_x_pos)
                viewer.setYpos(last_viewer_y_pos + 25)
    else:
        nuke.message("No viewer connected")
