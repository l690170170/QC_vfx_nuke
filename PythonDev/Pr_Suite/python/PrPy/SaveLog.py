"""
Script Name: SaveLog
Version: 1.0
Purpose: Record log of Nuke script's saving.
Created For: Pr_Suite v1.1
Create On: 11/05/2016
Author: Parimal Desai
Website: www.parimalvfx.com
History:
v1.0 (11/05/2016)
    Two functions to record and lock log.
"""

import time
import getpass
import platform
import os
import nuke


def save_log():
    """
    Record log of current Nuke script's saving.
    :return: None
    :rtype: None
    """
    clock = time.strftime("%I:%M %p")
    date = time.strftime("%d/%m/%Y")
    user = getpass.getuser()
    pc_name = platform.node()
    file_path = nuke.root()["name"].value()
    file_name = os.path.basename(file_path)
    root_label = nuke.root()["label"]
    existing_log = root_label.value()
    log = existing_log + "\n" + file_name + ", " + user + ", " + clock + ", " + date + ", " + pc_name
    root_label.setValue(log)
    root_label.setEnabled(False)


def lock_save_log():
    """
    Lock Root label.
    :return: None
    :rtype: None
    """
    nuke.root()["label"].setEnabled(False)
