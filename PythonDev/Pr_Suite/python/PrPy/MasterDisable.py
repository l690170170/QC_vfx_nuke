"""
Script Name: MasterDisable
Version: 1.1
Purpose: Disable multiple nodes with a single node.
Created For: Pr_Suite v1.1
Created On: 25/05/2016
Author: Parimal Desai
Website: www.parimalvfx.com
History:
v1.0 (12/09/2015)
    Disable multiple nodes by linking them to a disable knob in NoOp node.
v1.1 (25/05/2016)
    Added two PyScript_Knobs for filling Python fields in selected Write node to enable/disable NoOp node before and
    after render.
    Code optimization.
    PEP8 compliant.
"""

import nuke


def master_disable():
    """
    Link disable knob of all selected nodes to a newly created NoOp node's disable knob. With further options in NoOp
    node for disable control.
    :return: None
    :rtype: None
    """
    selected = nuke.selectedNodes()
    if len(selected) > 0:

        master = nuke.nodes.NoOp()
        master_name = master["name"].value()

        before = """selected = nuke.selectedNode()
if selected.Class() == "Write":
    code = "nuke.toNode('%s')['disable'].setValue(False)"
    selected["beforeRender"].setValue(code)
else:
    nuke.message("Please select a Write node.")
""" % master_name

        after = """selected = nuke.selectedNode()
if selected.Class() == "Write":
    code = "nuke.toNode('%s')['disable'].setValue(True)"
    selected["afterRender"].setValue(code)
else:
    nuke.message("Please select a Write node.")
""" % master_name

        tab = nuke.Tab_Knob("MasterDisable")
        disable = nuke.Boolean_Knob("disable", "disable", True)
        disable.setTooltip("Control disable of all connected nodes.")
        divider = nuke.Text_Knob("div", " ", "")
        set_before = nuke.PyScript_Knob("set_before", "Set Write Before Render", before)
        set_before.setTooltip("Set 'Before Render' of selected Write node to enable this Master Disable before render.")
        set_after = nuke.PyScript_Knob("set_after", "Set Write After Render", after)
        set_after.setTooltip("Set 'After Render' of selected Write node to disable this Master Disable after render.")

        for each in (tab, disable, divider, set_before, set_after):
            master.addKnob(each)

        master["hide_input"].setValue(True)
        master["label"].setValue("Master Disable - [value disable]")
        expression = "parent.%s.disable" % master_name
        for node in selected:
            node["disable"].setExpression(expression)
        master.showControlPanel()
    else:
        nuke.message("No nodes selected")
