"""
Script Name: CycleShuffleInOne
Version: 1.0
Purpose: Cycle Up/Down Shuffle node 'in 1' layer.
Created For: Bc_ToolSet v1.1
Created On: 04/05/2016
Author: Parimal Desai
Website: www.parimalvfx.com
History:
v1.0 (04/05/2016)
    First function to return node's layers and current layer's index.
    Two functions to Up/Down 'in 1' value.
"""

import nuke


def shuffle_in_layer_index(selected):
    """
    Find node's layers and index of 'in 1' layer's index.
    :param selected: Shuffle node
    :type selected: Node
    :return: List of node's layers and current 'in 1' layer's index.
    :rtype: tuple
    """
    layers = nuke.layers(selected)
    layers.insert(0, "none")
    shuffle_in = selected["in"].value()
    in_index = layers.index(shuffle_in)
    return layers, in_index


def shuffle_cycle_up():
    """
    Cycle Up Shuffle 'in 1' layers.
    :return: None
    :rtype: None
    """
    selected = nuke.selectedNode()
    if selected.Class() == "Shuffle":
        layers, in_index = shuffle_in_layer_index(selected)
        in_value = in_index - 1
        selected["in"].setValue(layers[in_value])
    else:
        nuke.message("'Cycle Shuffle in 1' only works with Shuffle node.")


def shuffle_cycle_down():
    """
    Cycle Down Shuffle 'in 1' layers.
    :return: None
    :rtype: None
    """
    selected = nuke.selectedNode()
    if selected.Class() == "Shuffle":
        layers, in_index = shuffle_in_layer_index(selected)
        in_value = in_index + 1
        if in_value >= len(layers):
            selected["in"].setValue("none")
        else:
            selected["in"].setValue(layers[in_value])
    else:
        nuke.message("'Cycle Shuffle in 1' only works with Shuffle node.")
