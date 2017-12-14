"""
Script Name: ShuffleEXRPasses
Version: 1.1
Purpose: Shuffle selected passes from a EXR Read node.
Created For: Bc_ToolSet v1.1
Created On: 13/05/2016
Author: Parimal Desai
Website: www.parimalvfx.com
History:
v1.0 (01/08/2015)
    Creates Shuffle nodes for all available passes, labels them accordingly and sets input to selected read node.
v1.1 (13/05/2016)
    Rewrote from scratch to build upon new concept.
    UI to shuffle out only selected passes.
    PEP8 compliant.
"""

import os
import nuke
import nukescripts


def find_node_layers(node):
    """
    Find layers of a Read node.
    :param node: Read node
    :type node: Node
    :return: List of layers in node.
    :rtype: list
    """
    node_channels = node.channels()
    store_layers = []
    for channel in node_channels:
        cut = channel.split(".")
        last = cut[0]
        store_layers.append(last)
    node_layers = list(set(store_layers))
    node_layers.sort()
    node_layers.remove("rgba")
    node_layers.insert(0, "rgba")
    return node_layers


class ShufflePassesPanel(nukescripts.PythonPanel):
    """
    UI and main operation.
    """
    def __init__(self):
        """
        Adding knobs to UI panel.
        """
        nukescripts.PythonPanel.__init__(self, "Shuffle EXR Passes", "com.parimalvfx.ShufflePassesPanel")

        self.node = nuke.selectedNode()
        self.nodeLayers = find_node_layers(self.node)
        self.layerKnobs = []

        for layer in self.nodeLayers:
            self.layer = nuke.Boolean_Knob(layer, layer, True)
            self.layer.setFlag(nuke.STARTLINE)
            self.addKnob(self.layer)
            self.layerKnobs.append(self.layer)
            if layer == "rgba":
                self.layer.setValue(False)

        self.div1 = nuke.Text_Knob("div1", " ", "")
        self.all = nuke.PyScript_Knob("select_all", " Select All ")
        self.invert = nuke.PyScript_Knob("invert_selection", " Invert Selection ")
        self.clear = nuke.PyScript_Knob("clear_selection", " Clear Selection ")
        self.div2 = nuke.Text_Knob("div2", " ", "")

        height = 125 + len(self.layerKnobs) * 20
        width = 330
        if height > 700:
            width = 350
            height = 700
        self.setMinimumSize(width, height)
        self.setMaximumSize(500, 900)

        for each in (self.div1, self.all, self.invert, self.clear, self.div2):
            self.addKnob(each)

    def knobChanged(self, knob):
        """
        Knob operations.
        :return: None
        :rtype: None
        """
        if knob.name() == "select_all":
            for layer in self.layerKnobs:
                layer.setValue(True)

        if knob.name() == "invert_selection":
            selected = []
            for layer in self.layerKnobs:
                if layer.value() is True:
                    selected.append(layer)
                    layer.setValue(False)
            inverse = list(set(self.layerKnobs).difference(set(selected)))
            for check in inverse:
                check.setValue(True)

        if knob.name() == "clear_selection":
            for layer in self.layerKnobs:
                layer.setValue(False)

        if knob.name() == "OK":
            extract = []
            for layer in self.layerKnobs:
                if layer.value() is True:
                    extract.append(layer.name())

            for layer in extract:
                shuffle = nuke.nodes.Shuffle(label=layer)
                shuffle["in"].setValue(layer)
                shuffle.setInput(0, self.node)


def launch():
    """
    Show UI
    :return: None
    :rtype: None
    """
    selected = nuke.selectedNode()
    if selected.Class() == "Read":
        if os.path.splitext(selected["file"].value())[1] == ".exr":
            launch_panel = ShufflePassesPanel()
            launch_panel.showModalDialog()
        else:
            nuke.message("Please select a Read node with EXR file")
    else:
        nuke.message("Please select a Read node")
