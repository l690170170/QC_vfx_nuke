"""
Script Name: NukeMultiFramesRender
Version: 1.0
Purpose: Render Nuke file in chunks.
Created For: Pr_Suite v1.1
Created On: 06/06/2016
Author: Parimal Desai
Website: www.parimalvfx.com
History:
v1.0 (06/06/2016)
    Render Nuke file into chunks by splitting frame range into given chunks and launching render for each chunk.
    Creates folder in TEMP for dumping render launching bat files.
"""

import getpass
import os
import sys
import random
import subprocess
import nuke

userName = getpass.getuser()
verFile = "C:/Users/%s/.nuke/nuke.ver" % userName

if os.path.isfile(verFile):

    ver = open(verFile, "r")
    verRead = ver.read()
    ver.close()

    verFolder = verRead.split(",")[0]
    verExe = verRead.split(",")[1]

    def frame_range_chunks(first, last, chunks):
        """
        Split given frame range into given chunks.
        """
        size = ((last - first + 1) + (chunks - 1)) // chunks
        while first <= last:
            following = first + size
            yield first, min(following - 1, last)
            first = following

    nukeFile = sys.argv[1]
    fileName = os.path.splitext(os.path.basename(nukeFile))[0]

    nuke.scriptOpen(nukeFile)

    allWrite = nuke.allNodes("Write")

    while len(allWrite) != 1:

        if len(allWrite) == 0:
            print "\nNo Write node found in current Nuke file, please keep one Write node in your Nuke file."
            nuke.scriptClose(nukeFile)
            break
        elif len(allWrite) > 1:
            print "\nMultiple Write nodes found, please keep only one Write node in your Nuke file."
            nuke.scriptClose(nukeFile)
            break

    else:
        if allWrite[0]["use_limit"].value() is True:
            writeFirst = allWrite[0]["first"].value()
            writeLast = allWrite[0]["last"].value()
            writeName = allWrite[0]["name"].value()
            nuke.scriptClose(nukeFile)

            print "\nYour frame range is: %s-%s" % (str(int(writeFirst)), str(int(writeLast)))

            userRange = raw_input("\nEnter frame range: ")
            userChunks = raw_input("\nChunks: ")

            firstInt = int(userRange.split("-")[0])
            lastInt = int(userRange.split("-")[1])
            chunksInt = int(userChunks)

            while chunksInt > 8:
                print "Up to 8 chunks are accepted, please enter chunks within this limit.\n"
                userChunks = raw_input("Chunks: ")
                chunksInt = int(userChunks)

            chunkRange = list(frame_range_chunks(firstInt, lastInt, chunksInt))

            tempPath = "C:/Users/%s/AppData/Local/Temp/Pr_SuiteTemp/" % userName

            tempSignal = 1
            if not os.path.isdir(tempPath):
                try:
                    os.mkdir(tempPath)
                except:
                    print "Can't proceed with rendering, something went wrong."
                    tempSignal = 0

            if tempSignal == 1:
                for chunk in chunkRange:
                    chunkFirst = str(chunk[0])
                    chunkLast = str(chunk[1])
                    uniqueNo = random.randint(0, 10000)
                    chunkName = tempPath + fileName + "_" + chunkFirst + "_" + chunkLast + "_" + str(uniqueNo) + ".bat"
                    chunkBat = open(chunkName, "w")
                    chunkBatCont = """@echo off
REM Pr_Suite Nuke Multi Frames Render v1.0 by Parimal Desai - www.parimalvfx.com
REM Setting terminal title, color and size
title Pr_Suite Nuke Multi Frames Render v1.0
color 80
c:
cd %s
cmd /k %s -F %s-%s -x %s"
""" % (verFolder, verExe, chunkFirst, chunkLast, nukeFile)
                    chunkBat.write(chunkBatCont)
                    chunkBat.close()
                    subprocess.Popen(chunkName, creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:
            print "\nPlease set 'limit to range' in your Write node to define render range."
            nuke.scriptClose(nukeFile)
else:
    print "\nPlease generate a 'nuke.ver' file from Pr_Suite menu inside Nuke before using Pr_Suite Nuke Render."
