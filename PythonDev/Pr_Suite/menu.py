"""
Script Name: menu
Version: 1.0
Purpose: Integrating Pr_Suite with Nuke GUI
Created For: Pr_Suite v1.1
Created On: 10/06/2016
Author: Parimal Desai
Website: www.parimalvfx.com
History:
v1.0 (10/06/2016)
    Integration of Pr_Suite with Nuke GUI driven by Pr_Suite Preferences.
"""

import os
import platform
import webbrowser
import nuke
from Preferences import platform_pref_path, launch as pref_launch
from RendersSetup import renders_setup
from PrPy import License, About

# Nodes Menu
nodesMenu = nuke.menu("Nodes")
nodes = nodesMenu.addMenu("Pr_Suite", icon="Pr_Suite_v01.png")

# Nuke Menu
topMenu = nuke.menu("Nuke")
top = topMenu.addMenu("Pr_Suite")

# Animation Menu
animation = nuke.menu("Animation")

# Viewer Menu
viewer = nuke.menu("Viewer")

# Preferences Condition
if os.path.exists(platform_pref_path()):  # Preferences Available
    import pr_suite_preferences as pref

    gizmoColor = pref.gizmo_color

    if pref.save_log is True:
        from PrPy.SaveLog import save_log, lock_save_log
        nuke.addOnScriptSave(save_log)
        nuke.addOnScriptLoad(lock_save_log)

    # Gizmos - Nodes Menu
    if pref.Pr_ShuffleMatte is True:
        Pr_ShuffleMatte = "nuke.createNode('Pr_ShuffleMatte', 'tile_color %d')" % gizmoColor
        nodes.addCommand("Pr_ShuffleMatte", Pr_ShuffleMatte, "", icon="Pr_ShuffleMatte_v01.png")
    if pref.Pr_LBGrain is True:
        Pr_LBGrain = "nuke.createNode('Pr_LBGrain', 'tile_color %d')" % gizmoColor
        nodes.addCommand("Pr_LBGrain", Pr_LBGrain, "", icon="Pr_LBGrain_v01.png")
    if pref.Pr_RGBLuma is True:
        Pr_RGBLuma = "nuke.createNode('Pr_RGBLuma', 'tile_color %d')" % gizmoColor
        nodes.addCommand("Pr_RGBLuma", Pr_RGBLuma, "", icon="Pr_RGBLuma_v01.png")
    if pref.Pr_RGBShadow is True:
        Pr_RGBShadow = "nuke.createNode('Pr_RGBShadow', 'tile_color %d')" % gizmoColor
        nodes.addCommand("Pr_RGBShadow", Pr_RGBShadow, "", icon="Pr_RGBShadow_v01.png")
    if pref.Pr_Contrast is True:
        Pr_Contrast = "nuke.createNode('Pr_Contrast', 'tile_color %d')" % gizmoColor
        nodes.addCommand("Pr_Contrast", Pr_Contrast, "", icon="Pr_Contrast_v01.png")
    if pref.Pr_Palette is True:
        Pr_Palette = "nuke.createNode('Pr_Palette', 'tile_color %d')" % gizmoColor
        nodes.addCommand("Pr_Palette", Pr_Palette, "", icon="Pr_Palette_v01.png")
    if pref.Pr_CameraAim is True:
        Pr_CameraAim = "nuke.createNode('Pr_CameraAim', 'tile_color %d')" % gizmoColor
        nodes.addCommand("Pr_CameraAim (Nuke 6, 7, 8)", Pr_CameraAim, "", icon="Pr_CameraAim_v01.png")
    if pref.Pr_CameraAim9 is True:
        Pr_CameraAim9 = "nuke.createNode('Pr_CameraAim9', 'tile_color %d')" % gizmoColor
        nodes.addCommand("Pr_CameraAim (Nuke 9, 10)", Pr_CameraAim9, "", icon="Pr_CameraAim_v01.png")
    if pref.Pr_LightAim is True:
        Pr_LightAim = "nuke.createNode('Pr_LightAim', 'tile_color %d')" % gizmoColor
        nodes.addCommand("Pr_LightAim (Nuke 6, 7, 8)", Pr_LightAim, "", icon="Pr_LightAim_v01.png")
    if pref.Pr_LightAim9 is True:
        Pr_LightAim9 = "nuke.createNode('Pr_LightAim9', 'tile_color %d')" % gizmoColor
        nodes.addCommand("Pr_LightAim (Nuke 9, 10)", Pr_LightAim9, "", icon="Pr_LightAim_v01.png")
    if pref.Pr_Timecode is True:
        Pr_Timecode = "nuke.createNode('Pr_Timecode', 'tile_color %d')" % gizmoColor
        nodes.addCommand("Pr_Timecode", Pr_Timecode, "", icon="Pr_Timecode_v01.png")
    if pref.Pr_InfoText is True:
        Pr_InfoText = "nuke.createNode('Pr_InfoText', 'tile_color %d')" % gizmoColor
        nodes.addCommand("Pr_InfoText", Pr_InfoText, "", icon="Pr_InfoText_v01.png")

    # Python - Nuke Menu
    if pref.node_graph_grid is True:
        from PrPy.NodeGraphGrid import node_graph_grid
        top.addCommand("Node Graph Grid", "node_graph_grid()", "Shift+H", icon="Node_Graph_Grid_v01.png")
    if pref.bring_down_viewer is True:
        from PrPy.BringDownViewer import bring_down_viewer
        top.addCommand("Bring Down Viewer", "bring_down_viewer()", "Shift+V", icon="Bring_Down_Viewer_v01.png")
    if pref.smart_floating_notepad is True:
        from PrPy.SmartFloatingNotepad import launch as sfn_launch
        top.addCommand("Smart Floating Notepad", "sfn_launch()", "Shift+N", icon="Smart_Floating_Notepad_v01.png")
    if pref.highlight_node is True:
        from PrPy.HighlightNode import highlight_node
        highlightNode = top.addMenu("Highlight Node", icon="Highlight_Node_v01.png")
        highlightNode.addCommand("Red", "highlight_node(0xff0000ff)", "F9", icon="Highlight_Node_Red_v01.png")
        highlightNode.addCommand("Green", "highlight_node(0xff00ff)", "F10", icon="Highlight_Node_Green_v01.png")
        highlightNode.addCommand("Blue", "highlight_node(0xffff)", "F11", icon="Highlight_Node_Blue_v01.png")
    if pref.master_disable is True:
        from PrPy.MasterDisable import master_disable
        top.addCommand("Master Disable", "master_disable()", "", icon="Master_Disable_v01.png")
    if pref.multi_knob_values is True:
        from PrPy.MultiKnobValues import launch as mnv_launch
        top.addCommand("Multi Knob Values", "mnv_launch()", "Alt+V", icon="Multi_Knob_Values_v01.png")
    if pref.cycle_merge_operation is True:
        from PrPy.CycleMergeOperation import cycle_up_merge_operation, cycle_down_merge_operation
        cycleMerge = top.addMenu("Cycle Merge Operation Up-Down", icon="Cycle_Merge_Operation_v01.png")
        cycleMerge.addCommand("Up", "cycle_up_merge_operation()", "Shift+PgUp", icon="Cycle_Up_v01.png")
        cycleMerge.addCommand("Down", "cycle_down_merge_operation()", "Shift+PgDown", icon="Cycle_Down_v01.png")
    if pref.cycle_shuffle_in is True:
        from PrPy.CycleShuffleInOne import shuffle_cycle_up, shuffle_cycle_down
        cycleShuffle = top.addMenu("Cycle Shuffle 'in 1' Up-Down", icon="Cycle_Shuffle_in1_v01.png")
        cycleShuffle.addCommand("Up", "shuffle_cycle_up()", "Ctrl+PgUp", icon="Cycle_Up_v01.png")
        cycleShuffle.addCommand("Down", "shuffle_cycle_down()", "Ctrl+PgDown", icon="Cycle_Down_v01.png")
    if pref.shuffle_exr_passes is True:
        from PrPy.ShuffleEXRPasses import launch as sp_launch
        top.addCommand("Shuffle EXR Passes", "sp_launch()", "Ctrl+E", icon="Shuffle_EXR_Passes_v01.png")
    if pref.label_shuffle is True:
        from PrPy.LabelShuffle import label_shuffle
        top.addCommand("Label Shuffle", "label_shuffle()", "Ctrl+L", icon="Label_v01.png")
    if pref.delete_error_read is True:
        from PrPy.DeleteErrorReads import delete_error_read
        top.addCommand("Delete all Read(s) with error", "delete_error_read()", "Ctrl+Shift+H",
                       icon="Delete_Thumbs_tmp_v01.png")
    if pref.delete_thumbs_tmp is True:
        from PrPy.DeleteErrorReads import delete_thumbs_tmp
        top.addCommand("Delete Thumbs.db and .tmp Read(s)", "delete_thumbs_tmp()", "Ctrl+Alt+H",
                       icon="Delete_Thumbs_tmp_v01.png")

    if pref.open_nuke_file_folder is True:
        from PrPy.OpenFolder import open_nuke_script
        top.addCommand("Open Nuke File Folder", "open_nuke_script()", "Shift+J", icon="Open_Folder_v01.png")


    top.addSeparator()
    top.addCommand("Preferences", "pref_launch()", icon="Preferences_v01.png")
    if platform.system() == "Windows":
        top.addCommand("Setup Pr_Suite Nuke Renders", "renders_setup()", icon="Preferences_v01.png")
        top.addSeparator()
    else:
        top.addSeparator()
    top.addCommand("Documentation", "About.docs()", icon="Doc.png")
    top.addCommand("Tutorials", "webbrowser.open('http://bitly.com/Pr_SuiteTutorials')", icon="Tutorials.png")
    top.addCommand("Report a Bug", "webbrowser.open('http://bit.ly/PrSuiteReportBug')", icon="Report_Bug_v01.png")
    top.addSeparator()
    top.addCommand("License", "License.pr_suite_license()", icon="Pr_Suite_v01.png")
    top.addCommand("About Pr_Suite", "About.about()", icon="Pr_Suite_v01.png")

    # Python - Animation Menu
    if pref.link_roto is True:
        from PrPy.LinkRotoBezier import launch as lrb_launch
        animation.addCommand("Link to Roto Bezier (Pr_Suite)", "lrb_launch()", icon="Link_Roto_Bezier_v01.png")
    if pref.forward_zero_one is True:
        from PrPy.SetFrames import forward_zero_one
        animation.addCommand("Set 0>1 (Pr_Suite)", "forward_zero_one()", icon="Set_Forward_v01.png")
    if pref.forward_one_zero is True:
        from PrPy.SetFrames import forward_one_zero
        animation.addCommand("Set 1>0 (Pr_Suite)", "forward_one_zero()", icon="Set_Forward_v01.png")
    if pref.backward_one_zero is True:
        from PrPy.SetFrames import backward_one_zero
        animation.addCommand("Set 1<0 (Pr_Suite)", "backward_one_zero()", icon="Set_Backward_v01.png")
    if pref.backward_zero_one is True:
        from PrPy.SetFrames import backward_zero_one
        animation.addCommand("Set 0<1 (Pr_Suite)", "backward_zero_one()", icon="Set_Backward_v01.png")
    if pref.one_zero_one is True:
        from PrPy.SetFrames import one_zero_one
        animation.addCommand("Set 1<0>1 (Pr_Suite)", "one_zero_one()", icon="Set_Backward_Forward_v01.png")
    if pref.zero_one_zero is True:
        from PrPy.SetFrames import zero_one_zero
        animation.addCommand("Set 0<1>0 (Pr_Suite)", "zero_one_zero()", icon="Set_Backward_Forward_v01.png")
    if pref.set_current_frame is True:
        from PrPy.SetFrames import set_current_frame
        animation.addCommand("Set Current Frame (Pr_Suite)", "set_current_frame()", icon="Set_Current_Frame_v01.png")

    # Python - Viewer Menu
    if pref.set_viewer_channel is True:
        from PrPy.ViewerOperations import set_rgba
        viewer.addCommand("Set Viewer channels to RGBA (Pr_Suite)", "set_rgba()", "F2", icon="RGBA_Channels_v01.png")
    if pref.set_ip_label is True:
        from PrPy.ViewerOperations import label_input_process
        viewer.addCommand("Set IP name as label (Pr_Suite)", "label_input_process()", "F3", icon="Label_v01.png")

else:  # Default Preferences
    # Gizmos - Nodes Menu
    nodes.addCommand("Pr_ShuffleMatte", "nuke.createNode('Pr_ShuffleMatte')", "", icon="Pr_ShuffleMatte_v01.png")
    nodes.addCommand("Pr_LBGrain", "nuke.createNode('Pr_LBGrain')", "", icon="Pr_LBGrain_v01.png")
    nodes.addCommand("Pr_RGBLuma", "nuke.createNode('Pr_RGBLuma')", "", icon="Pr_RGBLuma_v01.png")
    nodes.addCommand("Pr_RGBShadow", "nuke.createNode('Pr_RGBShadow')", "", icon="Pr_RGBShadow_v01.png")
    nodes.addCommand("Pr_Contrast", "nuke.createNode('Pr_Contrast')", "", icon="Pr_Contrast_v01.png")
    nodes.addCommand("Pr_Palette", "nuke.createNode('Pr_Palette')", "", icon="Pr_Palette_v01.png")
    nodes.addCommand("Pr_CameraAim (Nuke 6, 7, 8)", "nuke.createNode('Pr_CameraAim')", "", icon="Pr_CameraAim_v01.png")
    nodes.addCommand("Pr_CameraAim (Nuke 9, 10)", "nuke.createNode('Pr_CameraAim9')", "", icon="Pr_CameraAim_v01.png")
    nodes.addCommand("Pr_LightAim (Nuke 6, 7, 8)", "nuke.createNode('Pr_LightAim')", "", icon="Pr_LightAim_v01.png")
    nodes.addCommand("Pr_LightAim (Nuke 9, 10)", "nuke.createNode('Pr_LightAim9')", "", icon="Pr_LightAim_v01.png")
    nodes.addCommand("Pr_Timecode", "nuke.createNode('Pr_Timecode')", "", icon="Pr_Timecode_v01.png")
    nodes.addCommand("Pr_InfoText", "nuke.createNode('Pr_InfoText')", "", icon="Pr_InfoText_v01.png")

    # Python - Nuke Menu
    from PrPy.NodeGraphGrid import node_graph_grid
    top.addCommand("Node Graph Grid", "node_graph_grid()", "Shift+H", icon="Node_Graph_Grid_v01.png")
    from PrPy.BringDownViewer import bring_down_viewer
    top.addCommand("Bring Down Viewer", "bring_down_viewer()", "Shift+V", icon="Bring_Down_Viewer_v01.png")
    from PrPy.SmartFloatingNotepad import launch as sfn_launch
    top.addCommand("Smart Floating Notepad", "sfn_launch()", "Shift+N", icon="Smart_Floating_Notepad_v01.png")
    from PrPy.HighlightNode import highlight_node
    highlightNode = top.addMenu("Highlight Node", icon="Highlight_Node_v01.png")
    highlightNode.addCommand("Red", "highlight_node(0xff0000ff)", "F9", icon="Highlight_Node_Red_v01.png")
    highlightNode.addCommand("Green", "highlight_node(0xff00ff)", "F10", icon="Highlight_Node_Green_v01.png")
    highlightNode.addCommand("Blue", "highlight_node(0xffff)", "F11", icon="Highlight_Node_Blue_v01.png")
    from PrPy.MasterDisable import master_disable
    top.addCommand("Master Disable", "master_disable()", "", icon="Master_Disable_v01.png")
    from PrPy.MultiKnobValues import launch as mnv_launch
    top.addCommand("Multi Knob Values", "mnv_launch()", "Alt+V", icon="Multi_Knob_Values_v01.png")
    from PrPy.CycleMergeOperation import cycle_up_merge_operation, cycle_down_merge_operation
    cycleMerge = top.addMenu("Cycle Merge Operation Up-Down", icon="Cycle_Merge_Operation_v01.png")
    cycleMerge.addCommand("Up", "cycle_up_merge_operation()", "Shift+PgUp", icon="Cycle_Up_v01.png")
    cycleMerge.addCommand("Down", "cycle_down_merge_operation()", "Shift+PgDown", icon="Cycle_Down_v01.png")
    from PrPy.CycleShuffleInOne import shuffle_cycle_up, shuffle_cycle_down
    cycleShuffle = top.addMenu("Cycle Shuffle 'in 1' Up-Down", icon="Cycle_Shuffle_in1_v01.png")
    cycleShuffle.addCommand("Up", "shuffle_cycle_up()", "Ctrl+PgUp", icon="Cycle_Up_v01.png")
    cycleShuffle.addCommand("Down", "shuffle_cycle_down()", "Ctrl+PgDown", icon="Cycle_Down_v01.png")
    from PrPy.ShuffleEXRPasses import launch as sp_launch
    top.addCommand("Shuffle EXR Passes", "sp_launch()", "Ctrl+E", icon="Shuffle_EXR_Passes_v01.png")
    from PrPy.LabelShuffle import label_shuffle
    top.addCommand("Label Shuffle", "label_shuffle()", "Ctrl+L", icon="Label_v01.png")
    from PrPy.ReadFromWrite import read_from_write

    top.addCommand("Delete all Read(s) with error", "delete_error_read()", "Ctrl+Shift+H",
                   icon="Delete_Thumbs_tmp_v01.png")
    from PrPy.DeleteErrorReads import delete_thumbs_tmp
    top.addCommand("Delete Thumbs.db and .tmp Read(s)", "delete_thumbs_tmp()", "Ctrl+Alt+H",
                   icon="Delete_Thumbs_tmp_v01.png")

    from PrPy.OpenFolder import open_nuke_script
    top.addCommand("Open Nuke File Folder", "open_nuke_script()", "Shift+J", icon="Open_Folder_v01.png")
 
    
    top.addCommand("Preferences", "pref_launch()", "", icon="Preferences_v01.png")
    if platform.system() == "Windows":
        top.addCommand("Setup Pr_Suite Nuke Renders", "renders_setup()", icon="Preferences_v01.png")
        top.addSeparator()
    else:
        top.addSeparator()
    top.addCommand("Documentation", "About.docs()", icon="Doc.png")
    top.addCommand("Tutorials", "webbrowser.open('http://bitly.com/Pr_SuiteTutorials')", icon="Tutorials.png")
    top.addCommand("Report a Bug", "webbrowser.open('http://bit.ly/PrSuiteReportBug')", icon="Report_Bug_v01.png")
    top.addSeparator()
    top.addCommand("License", "License.pr_suite_license()", icon="Pr_Suite_v01.png")
    top.addCommand("About Pr_Suite", "About.about()", icon="Pr_Suite_v01.png")

    # Python - Animation Menu
    from PrPy.LinkRotoBezier import launch as lrb_launch
    animation.addCommand("Link to Roto Bezier (Pr_Suite)", "lrb_launch()", icon="Link_Roto_Bezier_v01.png")
    from PrPy.SetFrames import forward_zero_one
    animation.addCommand("Set 0>1 (Pr_Suite)", "forward_zero_one()", icon="Set_Forward_v01.png")
    from PrPy.SetFrames import forward_one_zero
    animation.addCommand("Set 1>0 (Pr_Suite)", "forward_one_zero()", icon="Set_Forward_v01.png")
    from PrPy.SetFrames import backward_one_zero
    animation.addCommand("Set 1<0 (Pr_Suite)", "backward_one_zero()", icon="Set_Backward_v01.png")
    from PrPy.SetFrames import backward_zero_one
    animation.addCommand("Set 0<1 (Pr_Suite)", "backward_zero_one()", icon="Set_Backward_v01.png")
    from PrPy.SetFrames import one_zero_one
    animation.addCommand("Set 1<0>1 (Pr_Suite)", "one_zero_one()", icon="Set_Backward_Forward_v01.png")
    from PrPy.SetFrames import zero_one_zero
    animation.addCommand("Set 0<1>0 (Pr_Suite)", "zero_one_zero()", icon="Set_Backward_Forward_v01.png")
    from PrPy.SetFrames import set_current_frame
    animation.addCommand("Set Current Frame (Pr_Suite)", "set_current_frame()", icon="Set_Current_Frame_v01.png")

    # Python - Viewer Menu
    from PrPy.ViewerOperations import set_rgba
    viewer.addCommand("Set Viewer channels to RGBA (Pr_Suite)", "set_rgba()", "F2", icon="RGBA_Channels_v01.png")
    from PrPy.ViewerOperations import label_input_process
    viewer.addCommand("Set IP name as label (Pr_Suite)", "label_input_process()", "F3", icon="Label_v01.png")

# Terminal Status
nuke.tprint("\nPr_Suite Loaded.\n")
