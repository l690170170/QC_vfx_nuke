"""
Script Name: DeleteErrorReads
Version: 1.0
Purpose: Functions to delete read nodes with error.
Created For: Pr_Suite v1.1
Created On: 30/05/2016
Author: Parimal Desai
Website: www.parimalvfx.com
History:
v1.0 (30/05/2016)
    Two functions with specific Read node deleting needs.
"""

import os
import nuke


def delete_error_read():
    """
    Delete all Read nodes with error.
    :return: None
    :rtype: None
    """
    all_nodes = nuke.allNodes("Read")
    for read in all_nodes:
        if read.error() is True:
            nuke.delete(read)


def delete_thumbs_tmp():
    """
    Delete all Thumbs.db and .tmp (extension) Read nodes.
    :return: None
    :rtype: None
    """
    all_nodes = nuke.allNodes("Read")
    for read in all_nodes:
        file_path = read["file"].value()
        last = os.path.basename(file_path)
        if last == "Thumbs.db" or last[-4:] == ".tmp":
            nuke.delete(read)
