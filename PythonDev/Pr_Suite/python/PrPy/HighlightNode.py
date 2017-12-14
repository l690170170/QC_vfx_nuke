"""
Script Name: HighlightNode
Version: v1.0
Purpose: Set defined color to selected nodes.
Created For: Pr_Suite v1.1
Created On: 04/05/2016
Author: Parimal Desai
Website: www.parimalvfx.com
Script History:
v1.0 (04/05/2016)
    Function to set defined color to selected nodes.
"""

import nuke


def highlight_node(color):
    """
    Toggle node tile color between user defined color and node's default color.
    :param color: Hexadecimal color code
    :type color: int
    :return: None
    :rtype: None
    """
    for node in nuke.selectedNodes():
        tile = node["tile_color"]
        if tile.value() == color:
            tile.setValue(nuke.defaultNodeColor(node.Class()))
        else:
            tile.setValue(color)
