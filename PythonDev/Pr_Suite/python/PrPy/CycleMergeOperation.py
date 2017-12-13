"""
Script Name: CycleMergeOperation
Version: 1.0
Purpose: Cycle Up/Down Merge Operation.
Created For: Pr_Suite v1.0
Created On: 05/05/2016
Author: Parimal Desai
Website: www.parimalvfx.com
History:
v1.0 (05/05/2016)
    Two functions to Up/Down 'Operation' value.
"""

import nuke


def cycle_up_merge_operation():
    """
    Cycle Up values of 'Operation' knob of Merge node.
    :return: None
    :rtype: None
    """
    selected = nuke.selectedNode()
    if selected.Class() == "Merge2":
        operation = selected["operation"]
        if int(operation.getValue()) - 1 >= 0:
            cycle_up = int(operation.getValue()) - 1
            operation.setValue(cycle_up)
        else:
            operation.setValue(29)
    else:
        nuke.message("'Cycle Merge Operation' only works with Merge node.")


def cycle_down_merge_operation():
    """
    Cycle Down values of 'Operation' knob of Merge node.
    :return: None
    :rtype: None
    """
    selected = nuke.selectedNode()
    if selected.Class() == "Merge2":
        operation = selected["operation"]
        if int(operation.getValue()) + 1 <= 29:
            cycle_down = int(operation.getValue()) + 1
            operation.setValue(cycle_down)
        else:
            operation.setValue(0)
    else:
        nuke.message("'Cycle Merge Operation' only works with Merge node.")
