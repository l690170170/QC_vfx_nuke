"""
Script Name: Preferences
Version: 1.0
Purpose: Bc_ToolSet preferences
Created For: Bc_ToolSet v1.1
Created On: 06/06/2016
Author: Parimal Desai
Website: www.parimalvfx.com
History:
v1.0 (06/06/2016)
    Bc_ToolSet preferences panel with ColorChip_Knob and Boolean_Knobs.
"""

import getpass
import platform
import os
import nuke
import nukescripts


def platform_pref_path():
    """
    Create path based on OS.
    :return: Preferences path
    :rtype: str
    """
    current_user = getpass.getuser()
    if platform.system() == "Windows":
        pref_path = "C:/Users/%s/.nuke/Bc_ToolSet_preferences.py" % current_user
        return pref_path
    elif platform.system() == "Darwin":
        pref_path = "Users/%s/.nuke/Bc_ToolSet_preferences.py" % current_user
        return pref_path
    elif platform.system() == "Linux":
        pref_path = "/home/%s/.nuke/Bc_ToolSet_preferences.py" % current_user
        return pref_path
    else:
        nuke.message("Unsupported OS")


class BcToolSetPreferencesPanel(nukescripts.PythonPanel):
    """
    UI and main operation.
    """
    def __init__(self):
        """
        Adding knobs to UI panel.
        """
        nukescripts.PythonPanel.__init__(self, "Bc_ToolSet Preferences", "com.parimalvfx.BcToolSetPreferencesPanel")

        self.setMinimumSize(450, 700)

        self.PrPref = nuke.Text_Knob("Bc_ToolSet_pref", "", "<font color='grey' size='7'><b>Bc_</b>ToolSet Preferences"
                                                          "</font><br>")
        self.div0 = nuke.Text_Knob("div0", "", " ")
        self.GzColor = nuke.ColorChip_Knob("gizmo_color", "  Gizmo Color ", 0x7f7f7fff)
        self.div1 = nuke.Text_Knob("div1", "", " ")
        self.div2 = nuke.Text_Knob("div2", "", "")
        self.PManager = nuke.Text_Knob("plugin_manager", "", "<br><font color='grey' size='5'><b>Plugin Manager</b>"
                                                             "</font><br>")
        self.SL = nuke.Boolean_Knob("save_log", "Nuke File Save Log", False)
        self.SL.setTooltip("Log information in Project Settings 'comment', whenever Nuke file saves.")
        self.Gizmos = nuke.Text_Knob("gizmos", "", "<br><font color='dark grey' size='4'><b>Gizmos</b></font>")
        self.ShuffleMatte = nuke.Boolean_Knob("Bc_ShuffleMatte", "Bc_ShuffleMatte", True)
        self.LBGrain = nuke.Boolean_Knob("Bc_LBGrain", "Bc_LBGrain", True)
        self.LBGrain.setFlag(nuke.STARTLINE)
        self.RGBLuma = nuke.Boolean_Knob("Bc_RGBLuma", "Bc_RGBLuma", True)
        self.RGBLuma.setFlag(nuke.STARTLINE)
        self.RGBShadow = nuke.Boolean_Knob("Bc_RGBShadow", "Bc_RGBShadow", True)
        self.RGBShadow.setFlag(nuke.STARTLINE)
        self.Contrast = nuke.Boolean_Knob("Bc_Contrast", "Bc_Contrast", True)
        self.Contrast.setFlag(nuke.STARTLINE)
        self.Palette = nuke.Boolean_Knob("Bc_Palette", "Bc_Palette", True)
        self.Palette.setFlag(nuke.STARTLINE)
        self.CameraAim = nuke.Boolean_Knob("Bc_CameraAim", "Bc_CameraAim (Nuke 6, 7, 8)", True)
        self.CameraAim.setFlag(nuke.STARTLINE)
        self.CameraAim9 = nuke.Boolean_Knob("Bc_CameraAim9", "Bc_CameraAim (Nuke 9, 10)", True)
        self.CameraAim9.setFlag(nuke.STARTLINE)
        self.LightAim = nuke.Boolean_Knob("Bc_LightAim", "Bc_LightAim (Nuke 6, 7, 8)", True)
        self.LightAim.setFlag(nuke.STARTLINE)
        self.LightAim9 = nuke.Boolean_Knob("Bc_LightAim9", "Bc_LightAim (Nuke 9, 10)", True)
        self.LightAim9.setFlag(nuke.STARTLINE)
        self.Timecode = nuke.Boolean_Knob("Bc_Timecode", "Bc_Timecode", True)
        self.Timecode.setFlag(nuke.STARTLINE)
        self.InfoText = nuke.Boolean_Knob("Bc_InfoText", "Bc_InfoText", True)
        self.InfoText.setFlag(nuke.STARTLINE)
        self.NukeMenu = nuke.Text_Knob("nuke_menu", "", "<br><font color='dark grey' size='4'><b>Python Scripts - Nuke"
                                                        " Menu</b></font>")
        self.NGG = nuke.Boolean_Knob("node_graph_grid", "Node Graph Grid", True)
        self.BDV = nuke.Boolean_Knob("bring_down_viewer", "Bring Down Viewer", True)
        self.BDV.setFlag(nuke.STARTLINE)
        self.SFN = nuke.Boolean_Knob("smart_floating_notepad", "Smart Floating Notepad", True)
        self.SFN.setFlag(nuke.STARTLINE)
        self.HN = nuke.Boolean_Knob("highlight_node", "Highlight Node", True)
        self.HN.setFlag(nuke.STARTLINE)
        self.MD = nuke.Boolean_Knob("master_disable", "Master Disable", True)
        self.MD.setFlag(nuke.STARTLINE)
        self.MKV = nuke.Boolean_Knob("multi_knob_values", "Multi Knob Values", True)
        self.MKV.setFlag(nuke.STARTLINE)
        self.CMO = nuke.Boolean_Knob("cycle_merge_operation", "Cycle Merge Operation Up-Down", True)
        self.CMO.setFlag(nuke.STARTLINE)
        self.CSI = nuke.Boolean_Knob("cycle_shuffle_in", "Cycle Shuffle 'in 1' Up-Down", True)
        self.CSI.setFlag(nuke.STARTLINE)
        self.SP = nuke.Boolean_Knob("shuffle_exr_passes", "Shuffle EXR Passes", True)
        self.SP.setFlag(nuke.STARTLINE)
        self.LS = nuke.Boolean_Knob("label_shuffle", "Label Shuffle", True)
        self.LS.setFlag(nuke.STARTLINE)
        self.RFW = nuke.Boolean_Knob("read_from_write", "Read from Write", True)
        self.RFW.setFlag(nuke.STARTLINE)
        self.DARE = nuke.Boolean_Knob("delete_error_read", "Delete all Read(s) with error", True)
        self.DARE.setFlag(nuke.STARTLINE)
        self.DATE = nuke.Boolean_Knob("delete_thumbs_tmp", "Delete Thumbs.db and .tmp Read(s)", True)
        self.DATE.setFlag(nuke.STARTLINE)
        self.ORF = nuke.Boolean_Knob("open_read_folder", "Open Read Folder", True)
        self.ORF.setFlag(nuke.STARTLINE)
        self.ONFF = nuke.Boolean_Knob("open_nuke_file_folder", "Open Nuke File Folder", True)
        self.ONFF.setFlag(nuke.STARTLINE)
        self.ODN = nuke.Boolean_Knob("open_dot_nuke", "Open .nuke Folder", True)
        self.ODN.setFlag(nuke.STARTLINE)
        self.OSPPF = nuke.Boolean_Knob("open_pp_folder", "Open Specific PLUGIN_PATH Folder", True)
        self.OSPPF.setFlag(nuke.STARTLINE)
        self.AnimationMenu = nuke.Text_Knob("animation_menu", "", "<br><font color='dark grey' size='4'><b>Python "
                                                                  "Scripts - Animation Menu</b></font>")
        self.LRB = nuke.Boolean_Knob("link_roto", "Link to Roto Bezier", True)
        self.SFZO = nuke.Boolean_Knob("forward_zero_one", "Set 0>1", True)
        self.SFZO.setFlag(nuke.STARTLINE)
        self.SF0Z = nuke.Boolean_Knob("forward_one_zero", "Set 1>0", True)
        self.SF0Z.setFlag(nuke.STARTLINE)
        self.SB0Z = nuke.Boolean_Knob("backward_one_zero", "Set 1<0", True)
        self.SB0Z.setFlag(nuke.STARTLINE)
        self.SBZO = nuke.Boolean_Knob("backward_zero_one", "Set 0<1", True)
        self.SBZO.setFlag(nuke.STARTLINE)
        self.SOZO = nuke.Boolean_Knob("one_zero_one", "Set 1<0>1", True)
        self.SOZO.setFlag(nuke.STARTLINE)
        self.SZOZ = nuke.Boolean_Knob("zero_one_zero", "Set 0<1>0", True)
        self.SZOZ.setFlag(nuke.STARTLINE)
        self.SCF = nuke.Boolean_Knob("set_current_frame", "Set Current Frame", True)
        self.SCF.setFlag(nuke.STARTLINE)
        self.ViewerMenu = nuke.Text_Knob("viewer_menu", "", "<br><font color='dark grey' size='4'><b>Python Scripts - "
                                                            "Viewer Menu</b></font>")
        self.SVC = nuke.Boolean_Knob("set_viewer_channel", "Set Viewer channels to RGBA", True)
        self.SIPL = nuke.Boolean_Knob("set_ip_label", "Set IP name as label", True)
        self.SIPL.setFlag(nuke.STARTLINE)
        self.div3 = nuke.Text_Knob("div3", "", " ")
        self.SavePref = nuke.PyScript_Knob("save_pref", " Save Preferences ")
        self.DefaultPref = nuke.PyScript_Knob("default_pref", " Set to Default ")

        if os.path.isfile(platform_pref_path()):
            import Bc_ToolSet_preferences as pref
            # Gizmo Color
            if pref.gizmo_color != 2139062271:
                self.GzColor.setValue(pref.gizmo_color)
            # Save Log
            if pref.save_log is True:
                self.SL.setValue(True)
            # Gizmos
            if pref.Bc_ShuffleMatte is False:
                self.ShuffleMatte.setValue(False)
            if pref.Bc_LBGrain is False:
                self.LBGrain.setValue(False)
            if pref.Bc_RGBLuma is False:
                self.RGBLuma.setValue(False)
            if pref.Bc_RGBShadow is False:
                self.RGBShadow.setValue(False)
            if pref.Bc_Contrast is False:
                self.Contrast.setValue(False)
            if pref.Bc_Palette is False:
                self.Palette.setValue(False)
            if pref.Bc_CameraAim is False:
                self.CameraAim.setValue(False)
            if pref.Bc_CameraAim9 is False:
                self.CameraAim9.setValue(False)
            if pref.Bc_LightAim is False:
                self.LightAim.setValue(False)
            if pref.Bc_LightAim9 is False:
                self.LightAim9.setValue(False)
            if pref.Bc_Timecode is False:
                self.Timecode.setValue(False)
            if pref.Bc_InfoText is False:
                self.InfoText.setValue(False)
            # Python Scripts - Nuke Menu
            if pref.node_graph_grid is False:
                self.NGG.setValue(False)
            if pref.bring_down_viewer is False:
                self.BDV.setValue(False)
            if pref.smart_floating_notepad is False:
                self.SFN.setValue(False)
            if pref.highlight_node is False:
                self.HN.setValue(False)
            if pref.master_disable is False:
                self.MD.setValue(False)
            if pref.multi_knob_values is False:
                self.MKV.setValue(False)
            if pref.cycle_merge_operation is False:
                self.CMO.setValue(False)
            if pref.cycle_shuffle_in is False:
                self.CSI.setValue(False)
            if pref.shuffle_exr_passes is False:
                self.SP.setValue(False)
            if pref.label_shuffle is False:
                self.LS.setValue(False)
            if pref.read_from_write is False:
                self.RFW.setValue(False)
            if pref.delete_error_read is False:
                self.DARE.setValue(False)
            if pref.delete_thumbs_tmp is False:
                self.DATE.setValue(False)
            if pref.open_read_folder is False:
                self.ORF.setValue(False)
            if pref.open_nuke_file_folder is False:
                self.ONFF.setValue(False)
            if pref.open_dot_nuke is False:
                self.ODN.setValue(False)
            if pref.open_pp_folder is False:
                self.OSPPF.setValue(False)
            # Python Scripts - Animation Menu
            if pref.link_roto is False:
                self.LRB.setValue(False)
            if pref.forward_zero_one is False:
                self.SFZO.setValue(False)
            if pref.forward_one_zero is False:
                self.SF0Z.setValue(False)
            if pref.backward_one_zero is False:
                self.SB0Z.setValue(False)
            if pref.backward_zero_one is False:
                self.SBZO.setValue(False)
            if pref.one_zero_one is False:
                self.SOZO.setValue(False)
            if pref.zero_one_zero is False:
                self.SZOZ.setValue(False)
            if pref.set_current_frame is False:
                self.SCF.setValue(False)
            # Python Scripts - Viewer Menu
            if pref.set_viewer_channel is False:
                self.SVC.setValue(False)
            if pref.set_ip_label is False:
                self.SIPL.setValue(False)

        for each in (self.PrPref, self.div0, self.GzColor, self.div1, self.div2, self.PManager, self.SL, self.Gizmos,
                     self.ShuffleMatte, self.LBGrain, self.RGBLuma, self.RGBShadow, self.Contrast, self.Palette,
                     self.CameraAim, self.CameraAim9, self.LightAim, self.LightAim9, self.Timecode, self.InfoText,
                     self.NukeMenu, self.NGG, self.BDV, self.SFN, self.HN, self.MD, self.MKV, self.CMO, self.CSI,
                     self.SP, self.LS, self.RFW, self.DARE, self.DATE, self.ORF, self.ONFF, self.ODN, self.OSPPF,
                     self.AnimationMenu, self.LRB, self.SFZO, self.SF0Z, self.SB0Z, self.SBZO, self.SOZO, self.SZOZ,
                     self.SCF, self.ViewerMenu, self.SVC, self.SIPL, self.div3, self.SavePref, self.DefaultPref):
            self.addKnob(each)

    def knobChanged(self, knob):
        """
        Knob operations.
        :return: None
        :rtype: None
        """
        if knob.name() == "save_pref":
            try:
                save_pref = open(platform_pref_path(), mode="w")
                save_pref.write("# Bc_ToolSet v1.1 Preferences")
                # Gizmo Color
                save_pref.write("\ngizmo_color = %d" % self.GzColor.value())
                # Save Log
                save_pref.write("\nsave_log = %s" % self.SL.value())
                # Gizmos
                save_pref.write("\nBc_ShuffleMatte = %s" % self.ShuffleMatte.value())
                save_pref.write("\nBc_LBGrain = %s" % self.LBGrain.value())
                save_pref.write("\nBc_RGBLuma = %s" % self.RGBLuma.value())
                save_pref.write("\nBc_RGBShadow = %s" % self.RGBShadow.value())
                save_pref.write("\nBc_Contrast = %s" % self.Contrast.value())
                save_pref.write("\nBc_Palette = %s" % self.Palette.value())
                save_pref.write("\nBc_CameraAim = %s" % self.CameraAim.value())
                save_pref.write("\nBc_CameraAim9 = %s" % self.CameraAim9.value())
                save_pref.write("\nBc_LightAim = %s" % self.LightAim.value())
                save_pref.write("\nBc_LightAim9 = %s" % self.LightAim9.value())
                save_pref.write("\nBc_Timecode = %s" % self.Timecode.value())
                save_pref.write("\nBc_InfoText = %s" % self.InfoText.value())
                # Python Scripts - Nuke Menu
                save_pref.write("\nnode_graph_grid = %s" % self.NGG.value())
                save_pref.write("\nbring_down_viewer = %s" % self.BDV.value())
                save_pref.write("\nsmart_floating_notepad = %s" % self.SFN.value())
                save_pref.write("\nhighlight_node = %s" % self.HN.value())
                save_pref.write("\nmaster_disable = %s" % self.MD.value())
                save_pref.write("\nmulti_knob_values = %s" % self.MKV.value())
                save_pref.write("\ncycle_merge_operation = %s" % self.CMO.value())
                save_pref.write("\ncycle_shuffle_in = %s" % self.CSI.value())
                save_pref.write("\nshuffle_exr_passes = %s" % self.SP.value())
                save_pref.write("\nlabel_shuffle = %s" % self.LS.value())
                save_pref.write("\nread_from_write = %s" % self.RFW.value())
                save_pref.write("\ndelete_error_read = %s" % self.DARE.value())
                save_pref.write("\ndelete_thumbs_tmp = %s" % self.DATE.value())
                save_pref.write("\nopen_read_folder = %s" % self.ORF.value())
                save_pref.write("\nopen_nuke_file_folder = %s" % self.ONFF.value())
                save_pref.write("\nopen_dot_nuke = %s" % self.ODN.value())
                save_pref.write("\nopen_pp_folder = %s" % self.OSPPF.value())
                # Python Scripts - Animation Menu
                save_pref.write("\nlink_roto = %s" % self.LRB.value())
                save_pref.write("\nforward_zero_one = %s" % self.SFZO.value())
                save_pref.write("\nforward_one_zero = %s" % self.SF0Z.value())
                save_pref.write("\nbackward_one_zero = %s" % self.SB0Z.value())
                save_pref.write("\nbackward_zero_one = %s" % self.SBZO.value())
                save_pref.write("\none_zero_one = %s" % self.SOZO.value())
                save_pref.write("\nzero_one_zero = %s" % self.SZOZ.value())
                save_pref.write("\nset_current_frame = %s" % self.SCF.value())
                # Python Scripts - Viewer Menu
                save_pref.write("\nset_viewer_channel = %s" % self.SVC.value())
                save_pref.write("\nset_ip_label = %s" % self.SIPL.value())
                save_pref.close()
                nuke.message("Preferences saved, please restart Nuke for preferences to take effect.")
            except:
                nuke.message("Can't save preferences, something went wrong")

        if knob.name() == "default_pref":
            if os.path.isfile(platform_pref_path()):
                os.remove(platform_pref_path())
                nuke.message("Preferences set to default, please restart Nuke for preferences to take effect.")
            else:
                nuke.message("Preferences is already set to to default.")


def launch():
    """
    Show UI
    :return: None
    :rtype: None
    """
    launch_panel = BcToolSetPreferencesPanel()
    launch_panel.showModal()
