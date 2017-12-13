"""
Script Name: ReadFromWrite
Version: 1.0
Purpose: Create Read node from selected Write node.
Created For: Pr_Suite v1.1
Created On: 11/05/2016
Author: Parimal Desai
Website: www.parimalvfx.com
History:
v1.0 (11/05/2016)
    Create's Read node with values from selected Write node.
"""

import nuke


def read_from_write():
    """
    Create Read node from selected Write node.
    :return: None
    :rtype: None
    """
    selected = nuke.selectedNode()
    if selected.Class() == "Write":
        if selected["use_limit"].value() is True:
            first_frame = selected["first"].value()
            last_frame = selected["last"].value()
        else:
            first_frame = nuke.Root()["first_frame"].value()
            last_frame = nuke.Root()["last_frame"].value()

        write = nuke.nodes.Read(
            file=selected["file"].value(),
            first=first_frame,
            last=last_frame,
            origfirst=nuke.Root()["first_frame"].value(),
            origlast=nuke.Root()["last_frame"].value())
        write.setXpos(selected.xpos()+100)
        write.setYpos(selected.ypos())
    else:
        nuke.message("Please select a Write node.")
