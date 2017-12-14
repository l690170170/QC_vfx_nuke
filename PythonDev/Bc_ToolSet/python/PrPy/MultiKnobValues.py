"""
Script Name: MultiKnobValues
Version: 1.1
Purpose: Get knob names and values from user and apply those values to selected nodes.
Created For: Bc_ToolSet v1.1
Created On: 25/05/2016
Author: Parimal Desai
Website: www.parimalvfx.com
History:
v1.0 (15/07/2015)
    Python panel with five string knobs for knob names and five array knobs for values.
    Setting values to selected nodes and checking for NameError and TypeError.
v1.1 (25/05/2016)
    Rewrote from scratch.
    Python panel with six string knobs for knob names, three array knobs and three string knobs for values.
    PEP8 compliant.
"""

import nuke
import nukescripts


class MultiKnobValuesPanel(nukescripts.PythonPanel):
    """
    UI and main operation.
    """
    def __init__(self):
        """
        Adding knobs to UI panel.
        """
        nukescripts.PythonPanel.__init__(self, "Multi Knob Values", "com.parimalvfx.MultiKnobValuesPanel")

        self.note = nuke.Text_Knob("note", "", "Enter knob calling Name and Value")
        self.div0 = nuke.Text_Knob("div0", "", " ")
        self.intFloat = nuke.Text_Knob("intFloat", "", "<font color='grey'><b>Integer/Float</b></font>")
        self.knob1 = nuke.String_Knob("knob1", "Knob 1")
        self.value1 = nuke.Array_Knob("value1", " = Value 1")
        self.value1.clearFlag(nuke.STARTLINE)
        self.knob2 = nuke.String_Knob("knob2", "Knob 2")
        self.value2 = nuke.Array_Knob("value2", " = Value 2")
        self.value2.clearFlag(nuke.STARTLINE)
        self.knob3 = nuke.String_Knob("knob3", "Knob 3")
        self.value3 = nuke.Array_Knob("value3", " = Value 3")
        self.value3.clearFlag(nuke.STARTLINE)
        self.div1 = nuke.Text_Knob("div1", "", " ")
        self.strEnu = nuke.Text_Knob("strEnu", "", "<font color='grey'><b>String/Enumeration</b></font>")
        self.knob4 = nuke.String_Knob("knob4", "Knob 4")
        self.value4 = nuke.String_Knob("value4", " = Value 4")
        self.value4.clearFlag(nuke.STARTLINE)
        self.knob5 = nuke.String_Knob("knob5", "Knob 5")
        self.value5 = nuke.String_Knob("value5", " = Value 5")
        self.value5.clearFlag(nuke.STARTLINE)
        self.knob6 = nuke.String_Knob("knob6", "Knob 6")
        self.value6 = nuke.String_Knob("value6", " = Value 6")
        self.value6.clearFlag(nuke.STARTLINE)
        self.div2 = nuke.Text_Knob("div2", "", " ")

        for each in (self.note, self.div0, self.intFloat, self.knob1, self.value1, self.knob2, self.value2, self.knob3,
                     self.value3, self.div1, self.strEnu, self.knob4, self.value4, self.knob5, self.value5, self.knob6,
                     self.value6, self.div2):
            self.addKnob(each)

    def knobChanged(self, knob):
        """
        Knob operations
        :return: None
        :rtype: None
        """
        if knob.name() == "OK":
            k1 = self.knob1.value()
            v1 = self.value1.value()
            k2 = self.knob2.value()
            v2 = self.value2.value()
            k3 = self.knob3.value()
            v3 = self.value3.value()
            k4 = self.knob4.value()
            v4 = self.value4.value()
            k5 = self.knob5.value()
            v5 = self.value5.value()
            k6 = self.knob6.value()
            v6 = self.value6.value()

            selected = nuke.selectedNodes()
            name_error = []
            type_error = []

            # Knob 1
            try:
                if k1 != "":
                    for each in selected:
                        each[k1].setValue(v1)
            except NameError:
                name_error.append("Knob 1: %s" % k1)
            except TypeError:
                type_error.append("Value 1: %s" % v1)
            except ValueError:
                type_error.append("Value 1: %s" % v1)
            else:
                pass

            # Knob 2
            try:
                if k2 != "":
                    for each in selected:
                        each[k2].setValue(v2)
            except NameError:
                name_error.append("Knob 2: %s" % k2)
            except TypeError:
                type_error.append("Value 2: %s" % v2)
            except ValueError:
                type_error.append("Value 2: %s" % v2)
            else:
                pass

            # Knob 3
            try:
                if k3 != "":
                    for each in selected:
                        each[k3].setValue(v3)
            except NameError:
                name_error.append("Knob 3: %s" % k3)
            except TypeError:
                type_error.append("Value 3: %s" % v3)
            except ValueError:
                type_error.append("Value 3: %s" % v3)
            else:
                pass

            # Knob 4
            try:
                if k4 != "":
                    for each in selected:
                        each[k4].setValue(v4)
            except NameError:
                name_error.append("Knob 4: %s" % k4)
            except TypeError:
                type_error.append("Value 4: %s" % v4)
            except ValueError:
                type_error.append("Value 4: %s" % v4)
            else:
                pass

            # Knob 5
            try:
                if k5 != "":
                    for each in selected:
                        each[k5].setValue(v5)
            except NameError:
                name_error.append("Knob 5: %s" % k5)
            except TypeError:
                type_error.append("Value 5: %s" % v5)
            except ValueError:
                type_error.append("Value 5: %s" % v5)
            else:
                pass

            # Knob 6
            try:
                if k6 != "":
                    for each in selected:
                        each[k6].setValue(v6)
            except NameError:
                name_error.append("Knob 6: %s" % k6)
            except TypeError:
                type_error.append("Value 6: %s" % v6)
            except ValueError:
                type_error.append("Value 6: %s" % v6)
            else:
                pass

            if len(name_error) or len(type_error) >= 1:
                if len(name_error) >= 1:
                    ne_str = ", ".join(name_error)
                else:
                    ne_str = "none"

                if len(type_error) >= 1:
                    te_str = ", ".join(type_error)
                else:
                    te_str = "none"

                error_msg = """Following knob and value input values has caused problem:

<b>Wrong calling name: <font color="red">%s</font></b>

<b>Wrong value type: <font color="red">%s</font></b>
""" % (str(ne_str), str(te_str))

                nuke.message(error_msg)


def launch():
    """
    Show UI
    :return: None
    :rtype: None
    """
    launch_panel = MultiKnobValuesPanel()
    launch_panel.showModalDialog()
