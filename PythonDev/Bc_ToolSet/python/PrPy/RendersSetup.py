"""
Script Name: RendersSetup
Version: 1.0
Purpose: Generates nuke.ver and bat files for launching renders.
Created For: Bc_ToolSet v1.1
Created On: 06/06/2016
Author: Parimal Desai
Website: www.parimalvfx.com
History:
v1.0 (06/06/2016)
    Generates nuke.ver file in .nuke directory with Nuke's exe path and name.
    Generates three bat files in shell:sendto for launching varieties of renders.
"""

import getpass
import os
import nuke


def renders_setup():
    """
    Configure Bc_ToolSet Nuke Renders.
    """
    try:
        user_name = getpass.getuser()
        ver_folder = os.path.dirname(nuke.env["ExecutablePath"])
        ver_exe = os.path.splitext(os.path.basename(nuke.env["ExecutablePath"]))[0]

        if nuke.ask("Your Bc_ToolSet Nuke Renders will be configured <b>%s</b>, please click Yes to continue." % ver_exe):

            # VER FILE
            ver_write = ver_folder + "," + ver_exe
            ver_file = "C:/Users/%s/.nuke/nuke.ver" % user_name
            ver = open(ver_file, "w")
            ver.write(ver_write)
            ver.close()

            # BAT FILE - Bc_ToolSet NUKE FULL RENDER V1.0
            fr_bat_file = "C:/Users/%s/AppData/Roaming/Microsoft/Windows/SendTo/Bc_ToolSet Nuke Full Render.bat" \
                          % user_name
            fr_bat = open(fr_bat_file, "w")
            fr_bat_cont = """@echo off
REM Bc_ToolSet Nuke Full Render v1.0 by Parimal Desai - www.parimalvfx.com
REM Setting terminal title, color and size
title Bc_ToolSet Nuke Full Render v1.0
color 80
mode con: cols=100 lines=1000
echo ____________________________________________________________________________________________________
echo                                   Bc_ToolSet Nuke Full Render v1.0
echo ____________________________________________________________________________________________________
c:
cd %s
cmd /k %s -x %%1
""" % (ver_folder, ver_exe)
            fr_bat.write(fr_bat_cont)
            fr_bat.close()

            # BAT FILE - Bc_ToolSet NUKE MULTI FRAMES RENDER V1.0
            mfr_python = "C:/Users/%s/.nuke/Bc_ToolSet/python/NukeMultiFramesRender.py" % user_name
            mfr_bat_file = "C:/Users/%s/AppData/Roaming/Microsoft/Windows/SendTo/Bc_ToolSet Nuke Multi Frames " \
                           "Render.bat" % user_name
            mfr_bat = open(mfr_bat_file, "w")
            mfr_bat_cont = """@echo off
REM Bc_ToolSet Nuke Multi Frames Render v1.0 by Parimal Desai - www.parimalvfx.com
REM Setting terminal title, color and size
title Bc_ToolSet Nuke Multi Frames Render v1.0
color 80
mode con: cols=80 lines=20
echo ________________________________________________________________________________
echo                     Bc_ToolSet Nuke Multi Frames Render v1.0
echo ________________________________________________________________________________
c:
cd %s
cmd /k %s -t %s %%1
""" % (ver_folder, ver_exe, mfr_python)
            mfr_bat.write(mfr_bat_cont)
            mfr_bat.close()

            # BAT FILE - Bc_ToolSet NUKE QUEUE RENDER V1.0
            qr_python = "C:/Users/%s/.nuke/Bc_ToolSet/python/NukeQueueRender.py" % user_name
            qr_bat_file = "C:/Users/%s/AppData/Roaming/Microsoft/Windows/SendTo/Bc_ToolSet Nuke Queue " \
                          "Render.bat" % user_name
            qr_bat = open(qr_bat_file, "w")
            qr_bat_cont = """@echo off
REM Bc_ToolSet Nuke Queue Render v1.0 by Parimal Desai - www.parimalvfx.com
REM Setting terminal title, color and size
title Bc_ToolSet Nuke Queue Render v1.0
color 80
mode con: cols=120 lines=5000
echo ________________________________________________________________________________________________________________________
echo                                             Bc_ToolSet Nuke Queue Render v1.0
echo ________________________________________________________________________________________________________________________
c:
cd %s
cmd /k %s -t %s %%1
""" % (ver_folder, ver_exe, qr_python)
            qr_bat.write(qr_bat_cont)
            qr_bat.close()

            # BAT FILE - Bc_ToolSet NUKE RENDERS DOCUMENTATION
            doc_bat_file = "C:/Users/%s/AppData/Roaming/Microsoft/Windows/SendTo/Bc_ToolSet Nuke Renders " \
                           "Documentation.bat" % user_name
            doc_bat = open(doc_bat_file, "w")
            doc_bat_cont = """@echo off
start "" "C:\Users\%s\.nuke\Bc_ToolSet\documentation\Bc_ToolSetNukeRendersWindowsOnly.html"
""" % user_name
            doc_bat.write(doc_bat_cont)
            doc_bat.close()

            # CONFIGURATION MESSAGE
            nuke.message("""Your Bc_ToolSet Nuke Renders are configured with <b>%s</b>

To change Nuke version for Bc_ToolSet Nuke Renders please setup the same from your desired Nuke version.

Following Renders are now available for your rendering needs:

    &#8226; Bc_ToolSet Nuke Full Render v1.0
    &#8226; Bc_ToolSet Nuke Multi Frames Render v1.0
    &#8226; Bc_ToolSet Nuke Queue Render v1.0

""" % ver_exe)

    except:
        nuke.message("Something went wrong while configuring Bc_ToolSet Nuke Renders, please read documentation for "
                     "possible solutions or contact developer for further support.")
