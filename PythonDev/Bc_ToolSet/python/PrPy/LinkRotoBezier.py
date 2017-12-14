"""
Script Name: LinkRotoBezier
Version: 1.0
Purpose: Link XY_Knob to a Roto Bezier.
Created For: Bc_ToolSet v1.1
Created On: 10/05/2016
Author: Parimal Desai
Website: www.parimalvfx.com
History:
v1.0 (10/05/2016)
    Python panel with roto and bezier selection.
    Linking selected XY_Knob to selected roto bezier.
    Adding UI to selected node for bezier animation control.
"""

import nuke
import nukescripts


class RotoBezier(nukescripts.PythonPanel):
    """
    UI and Main operation.
    """
    def __init__(self):
        """
        Adding knobs to UI panel.
        """
        nukescripts.PythonPanel.__init__(self, "Select Roto & Bezier")

        roto_list = []
        for each in nuke.allNodes("Roto"):
            roto_list.append(each["name"].value())
        roto_list.sort()
        self.roto = nuke.Enumeration_Knob("roto_list", "Select Roto Node", roto_list)
        self.bezier = nuke.Enumeration_Knob("bezier_list", "Select Bezier Shape", [])

        for add in (self.roto, self.bezier):
            self.addKnob(add)

    def show(self):
        """
        Node bezier animation UI and expression setting.
        :return: None
        :rtype: None
        """
        if nukescripts.PythonPanel.showModalDialog(self):

            def link_to_bezier(selected_roto, selected_bezier):
                """
                Node bezier animation UI and expression setting.
                :param selected_roto: Roto node name
                :type selected_roto: str
                :param selected_bezier: Bezier name
                :type selected_bezier: str
                :return: None
                :rtype: None
                """
                this_knob = nuke.thisKnob()
                this_node = nuke.thisNode()

                tab = nuke.Tab_Knob("BezierAnimation")
                slider = nuke.Double_Knob("bezier_animation", "Bezier Animation")
                slider.setTooltip("Animate along bezier shape from start to end.")
                this_node.addKnob(tab)
                this_node.addKnob(slider)

                x_expression = """
[python -execlocal {
try:
    shape = nuke.toNode('%s')['curves'].toElement('%s').evaluate(0, nuke.frame())
except:
    pass
ret = shape.getPoint(nuke.thisNode()['bezier_animation'].value()).x
}]
""" % (selected_roto, selected_bezier)

                y_expression = """
[python -execlocal {
try:
    shape = nuke.toNode('%s')['curves'].toElement('%s').evaluate(0, nuke.frame())
except:
    pass
ret = shape.getPoint(nuke.thisNode()['bezier_animation'].value()).y
}]
""" % (selected_roto, selected_bezier)

                this_knob.setExpression(x_expression, channel=0)
                this_knob.setExpression(y_expression, channel=1)
                try:
                    this_node["center"].setValue(0)
                except:
                    pass

            link_to_bezier(self.roto.value(), self.bezier.value())

    def knobChanged(self, knob):
        """
        Knob operations.
        :return: None
        :rtype: None
        """
        if knob.name() == "roto_list" or "bezier_list":
            bezier_list = []
            selected_roto = self.roto.value()
            roto_shapes = nuke.toNode(selected_roto)["curves"].rootLayer
            for each in roto_shapes:
                bezier_list.append(each.name)
            bezier_list.sort()
            self.bezier.setValues(bezier_list)


def launch():
    """
    Show UI
    :return: None
    :rtype: None
    """
    this_knob = nuke.thisKnob()
    if str(type(this_knob)) == "<type 'XY_Knob'>":
        if len(nuke.allNodes("Roto")) >= 1:
            RotoBezier().show()
        else:
            nuke.message("No Roto node found, please create a Roto node with a Bezier.")
    else:
        nuke.message("'Link to Roto Bezier' only works with XY Knob, such as translate knob of Translate node.")
