"""
Script Name: NodeGraphGrid
Version: 1.1
Purpose: Toggle enable/disable show grid and snap to grid.
Created For: Bc_ToolSet v1.1
Created On: 15/05/2016
Author: Parimal Desai
Website: www.parimalvfx.com
History:
v1.0 (28/07/2015)
    Enable/Disable show grid and snap to grid.
v1.1 (15/05/2016)
    Code optimization.
    PEP8 compliant.
"""

import nuke


def node_graph_grid():
    """
    Toggle enable/disable show grid and snap to grid.
    :return: None
    :rtype: None
    """
    show = nuke.toNode("preferences").knob("show_grid")
    snap = nuke.toNode("preferences").knob("SnapToGrid")
    if show.value() and snap.value() is True:
        show.setValue(0)
        snap.setValue(0)
    else:
        show.setValue(1)
        snap.setValue(1)
