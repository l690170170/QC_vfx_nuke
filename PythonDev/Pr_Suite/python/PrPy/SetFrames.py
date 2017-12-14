"""
Script Name: SetFrames
Version: 1.0
Purpose: Find value of previous, current and next frames and set keys on selected knob.
Created For: Pr_Suite v1.1
Created On: 01/05/2016
Author: Parimal Desai
Website: www.parimalvfx.com
Script:
v1.0 (01/05/2016)
    First function to find value of previous, current and next frame.
    Rest functions for their specified operations.
"""

import nuke


def previous_current_next_frame():
    """
    Find previous frame and next frame from current frame.
    :return: Values of  previous, current and next frame.
    :rtype: tuple
    """
    current_frame = nuke.frame()
    previous_frame = current_frame - 1
    next_frame = current_frame + 1
    return previous_frame, current_frame, next_frame


def set_current_frame():
    """
    Set value of current frame to selected Array Knob.
    :return: None
    :rtype: None
    """
    knob = nuke.thisKnob()
    knob_type = str(type(knob))
    if knob_type == "<type 'Array_Knob'>":
        knob.setValue(previous_current_next_frame()[1])
    else:
        nuke.message("'Set Current Frame' only work's with Array Knob, such as first frame knob of FrameHold node.")


def forward_zero_one():
    """
    Animate selected knob's value at current frame to 0 and next frame to 1.
    :return: None
    :rtype: None
    """
    knob = nuke.thisKnob()
    knob.setAnimated()
    knob.setValueAt(0, previous_current_next_frame()[1])
    knob.setValueAt(1, previous_current_next_frame()[2])


def forward_one_zero():
    """
    Animate selected knob's value at current frame to 1 and next frame to 0.
    :return: None
    :rtype: None
    """
    knob = nuke.thisKnob()
    knob.setAnimated()
    knob.setValueAt(1, previous_current_next_frame()[1])
    knob.setValueAt(0, previous_current_next_frame()[2])


def backward_one_zero():
    """
    Animate selected knob's value at previous frame to 1 and current frame to 0.
    :return: None
    :rtype: None
    """
    knob = nuke.thisKnob()
    knob.setAnimated()
    knob.setValueAt(1, previous_current_next_frame()[0])
    knob.setValueAt(0, previous_current_next_frame()[1])


def backward_zero_one():
    """
    Animate selected knob's value at previous frame to 0 and current frame to 1.
    :return: None
    :rtype: None
    """
    knob = nuke.thisKnob()
    knob.setAnimated()
    knob.setValueAt(0, previous_current_next_frame()[0])
    knob.setValueAt(1, previous_current_next_frame()[1])


def one_zero_one():
    """
    Animate selected knob's value at previous frame to 1, current frame to 0 and next frame to 1.
    :return: None
    :rtype: None
    """
    knob = nuke.thisKnob()
    knob.setAnimated()
    knob.setValueAt(1, previous_current_next_frame()[0])
    knob.setValueAt(0, previous_current_next_frame()[1])
    knob.setValueAt(1, previous_current_next_frame()[2])


def zero_one_zero():
    """
    Animate selected knob's value at previous frame to 0, current frame to 1 and next frame to 0.
    :return: None
    :rtype: None
    """
    knob = nuke.thisKnob()
    knob.setAnimated()
    knob.setValueAt(0, previous_current_next_frame()[0])
    knob.setValueAt(1, previous_current_next_frame()[1])
    knob.setValueAt(0, previous_current_next_frame()[2])
