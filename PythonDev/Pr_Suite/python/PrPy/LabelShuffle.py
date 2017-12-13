"""
Script Name: LabelShuffle
Version: 1.1
Purpose: Label Shuffle node with value of knob 'in 1'.
Created For: Pr_Suite v1.1
Created On: 15/05/2016
Author: Parimal Desai
Website: www.parimalvfx.com
History:
v1.0 (12/09/2015)
    Label Shuffle node with value of knob 'in 1'.
v1.1 (15/05/2016)
    Code optimization.
    PEP8 compliant.
"""

import nuke


def label_shuffle():
    """
    Label selected Shuffle node with value of knob 'in 1'.
    :return: None
    :rtype: None
    """
    selected = nuke.selectedNode()
    if selected.Class() == "Shuffle":
        selected["label"].setValue("[value in]")
    else:
        nuke.message("Please select a Shuffle node")
