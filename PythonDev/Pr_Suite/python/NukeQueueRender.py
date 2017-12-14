"""
Script Name: NukeQueueRender
Version: 1.0
Purpose: Queue Nuke files for rendering from a directory.
Created For: Pr_Suite v1.1
Created On: 06/06/2016
Author: Parimal Desai
Website: www.parimalvfx.com
History:
v1.0 (06/06/2016)
    Renders every Nuke file from given directory and its subdirectories one by one, and if error occurs skips to next.
"""

import sys
import os
import fnmatch
import time
import nuke

folderPath = sys.argv[1]

nukeFiles = []

for root, dirnames, filenames in os.walk(folderPath):
    for filename in fnmatch.filter(filenames, "*.nk"):
        nukeFiles.append(os.path.join(root, filename))

if len(nukeFiles) >= 1:
    print "\n\nTotal Nuke files in directory: %d" % len(nukeFiles)
    print "\nStarting render jobs..."
    print "\nRender jobs started at %s" % time.strftime("%I:%M %p %d/%m/%Y")
    print "\n\n-----------------------------------------------------------------------------------------" \
          "-------------------------------"
    renderedJobs = []
    setLimit = []
    noWrite = []
    for eachFile in nukeFiles:
        basename = os.path.basename(eachFile)
        nuke.scriptOpen(eachFile)
        allWrite = nuke.allNodes("Write")
        if len(allWrite) >= 1:
            for eachWrite in allWrite:
                writeName = eachWrite["name"].value()
                if eachWrite["use_limit"].value() is True:
                    writeFirst = eachWrite["first"].value()
                    writeLast = eachWrite["last"].value()
                    print "Starting render job for: File - %s, Write Node - %s\n" % (basename, writeName)
                    nuke.execute(writeName, int(writeFirst), int(writeLast))
                    print "-----------------------------------------------------------------------------------------" \
                          "-------------------------------"
                    renderedJobs.append(writeName)
                else:
                    print "Please set 'limit to range' in '%s' Write node of file '%s', skipping to next render job." \
                          % (writeName, basename)
                    print "-----------------------------------------------------------------------------------------" \
                          "-------------------------------"
                    setLimit.append([basename, writeName])
            nuke.scriptClose(eachFile)
        elif len(allWrite) < 1:
            print "No Write node found in '%s', skipping to next render job" % basename
            nuke.scriptClose(eachFile)
            print "-----------------------------------------------------------------------------------------" \
                  "-------------------------------"
            noWrite.append(basename)
            continue

    print "\nRender jobs completed at %s" % time.strftime("%I:%M %p %d/%m/%Y")
    print "\nTotal render jobs completed: %d" % len(renderedJobs)
    print "\nTotal render jobs skipped: %d" % len(noWrite + setLimit)
    if len(noWrite + setLimit) >= 1:
        print "\nSkipped render jobs log:"
        for skipped in noWrite:
            print "  *" + skipped, "- No Write node exists"
        for skipped in setLimit:
            print "  *" + skipped[0], "- Set 'limit to range' in %s" % skipped[1]
        print "\n"

else:
    print "\n\nNo Nuke files found in selected folder."
