"""
Script Name: SmartFloatingNotepad
Version: 1.0
Purpose: Floating notepad with comparing and bookmarking features.
Created For: Bc_ToolSet v1.1
Created On: 25/05/2016
Author: Parimal Desai
Website: www.parimalvfx.com
History:
v1.0 (25/05/2016)
    Python panel notepad with comparing and bookmarking features.
"""

import getpass
import platform
import time
import os
import nuke
import nukescripts


def platform_bookmark_path():
    """
    Create path based on OS.
    :return: Directory path
    :rtype: str
    """
    current_user = getpass.getuser()
    if platform.system() == "Windows":
        save_path = "C:/Users/%s/.nuke/FloatingNotepadBookmarks" % current_user
        return save_path
    elif platform.system() == "Darwin":
        save_path = "Users/%s/.nuke/FloatingNotepadBookmarks" % current_user
        return save_path
    elif platform.system() == "Linux":
        save_path = "/home/%s/.nuke/FloatingNotepadBookmarks" % current_user
        return save_path
    else:
        nuke.message("Unsupported OS")


def save_bookmark(path, bookmark):
    """
    Save bookmark.
    :param path: Default bookmark directory path.
    :type path: str
    :param bookmark: Bookmark content
    :type bookmark: str
    :return: None
    :rtype: None
    """
    try:
        bmk_name = time.strftime("%d_%m_%Y_%I_%M_%S_%p")
        get_name = nuke.getInput("Bookmark as...", bmk_name)
        if get_name:
            bmk_path = path + "/" + get_name + ".txt"
            save_bmk = open(bmk_path, mode="w")
            save_bmk.write(bookmark)
            save_bmk.close()
            nuke.message("Bookmarked as '%s'" % get_name)
    except:
        nuke.message("Can't bookmark, something went wrong.")


def base_bookmark_list(path):
    """
    List all available bookmarks.
    :param path: Directory path
    :type path: str
    :return: List of all available bookmarks.
    :rtype: list
    """
    all_bmk = os.listdir(path)
    bmk_base = []
    for each in all_bmk:
        bmk_base.append(os.path.splitext(each)[0])
    bmk_base.insert(0, "Select Bookmark")
    return bmk_base


class SmartFloatingNotepadPanel(nukescripts.PythonPanel):
    """
    UI and main operation.
    """
    def __init__(self):
        """
        Adding knobs to UI panel.
        """
        nukescripts.PythonPanel.__init__(self, "Smart Floating Notepad", "com.parimalvfx.SmartFloatingNotepadPanel")

        self.notepadOne = nuke.Multiline_Eval_String_Knob("first_notepad", "")
        self.notepadOne.setTooltip("Take your notes here...")
        self.notepadTwo = nuke.Multiline_Eval_String_Knob("second_notepad", "")
        self.notepadTwo.setTooltip("Compare notes with first notepad")
        self.notepadTwo.clearFlag(nuke.STARTLINE)
        self.notepadTwo.setVisible(False)
        self.options = nuke.Boolean_Knob("options", "Options", True)
        self.options.setTooltip("Toggle notepad options")
        self.options.setFlag(nuke.STARTLINE)
        self.compare = nuke.PyScript_Knob("compare", "Compare Notes")
        self.compare.setTooltip("Toggle second notepad")
        self.compare.setFlag(nuke.STARTLINE)
        self.bookmark = nuke.PyScript_Knob("bookmark", "Bookmark")
        self.bookmark.setTooltip("Bookmark first notepad's notes.")
        self.bookmarkList = nuke.Enumeration_Knob("bookmark_list", "", [])
        self.bookmarkList.setTooltip("Open bookmarked notes in second notepad.")
        self.bookmarkList.clearFlag(nuke.STARTLINE)
        self .clearBookmark = nuke.PyScript_Knob("clear_bookmark", "Clear Bookmark")

        self.addKnob(self.notepadOne)
        self.addKnob(self.notepadTwo)
        self.addKnob(self.options)
        self.addKnob(self.compare)
        self.addKnob(self.bookmark)
        self.addKnob(self.bookmarkList)
        self.addKnob(self.clearBookmark)

    def knobChanged(self, knob):
        """
        Knob operations
        :return: None
        :rtype: None
        """
        if knob.name() == "showPanel":
            if not os.path.isdir(platform_bookmark_path()):
                os.mkdir(platform_bookmark_path())
            self.bookmarkList.setValues(base_bookmark_list(platform_bookmark_path()))

        if knob.name() == "options":
            if self.options.value() is True:
                self.compare.setVisible(True)
                self.bookmark.setVisible(True)
                self.bookmarkList.setVisible(True)
                self.clearBookmark.setVisible(True)
            else:
                self.compare.setVisible(False)
                self.bookmark.setVisible(False)
                self.bookmarkList.setVisible(False)
                self.clearBookmark.setVisible(False)

        if knob.name() == "compare":
            if self.notepadTwo.visible() is False:
                self.notepadTwo.setVisible(True)
            else:
                self.notepadTwo.setVisible(False)

        if knob.name() == "bookmark":
            save_bookmark(platform_bookmark_path(), self.notepadOne.value())
            self.bookmarkList.setValues(base_bookmark_list(platform_bookmark_path()))

        if knob.name() == "bookmark_list":
            selected_bmk = self.bookmarkList.value()
            if not selected_bmk == "Select Bookmark":
                try:
                    selected_bmk_path = platform_bookmark_path() + "/" + selected_bmk + ".txt"
                    open_bmk = open(selected_bmk_path, "r")
                    bmk_value = open_bmk.read()
                    open_bmk.close()
                    self.notepadTwo.setVisible(True)
                    self.notepadTwo.setValue(bmk_value)
                except:
                    nuke.message("Something went wrong while opening bookmark '%s'." % selected_bmk)
            else:
                self.notepadTwo.setValue("")

        if knob.name() == "clear_bookmark":
            selected_bmk = self.bookmarkList.value()
            if not selected_bmk == "Select Bookmark":
                try:
                    selected_bmk_path = platform_bookmark_path() + "/" + selected_bmk + ".txt"
                    os.remove(selected_bmk_path)
                    nuke.message("Cleared bookmark '%s'" % selected_bmk)
                    self.bookmarkList.setValues(base_bookmark_list(platform_bookmark_path()))
                    self.notepadTwo.setValue("")
                    self.bookmarkList.setValue("Select Bookmark")
                except:
                    nuke.message("Something went wrong while clearing bookmark '%s'." % selected_bmk)


def launch():
    """
    Show UI
    :return: None
    :rtype: None
    """
    launch_panel = SmartFloatingNotepadPanel()
    launch_panel.show()
