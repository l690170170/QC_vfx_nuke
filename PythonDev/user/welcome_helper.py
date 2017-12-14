# -*- coding: utf-8 -*-
# __author__ = 'XingHuan'
# 2017/3/3
import os
import shutil
import welcome_path as wp
import welcome_setting as ws

Current_User = os.path.expanduser('~').replace('\\','/').split("/")[-1]
Recent_Files = "%s/%s/recent_files" % (wp.Users_Path, Current_User)

def createFolder():
    recentFilesPath = "%s/%s" % (wp.Users_Path, Current_User)
    if os.path.exists(recentFilesPath) ==False:
        os.makedirs(recentFilesPath)
    if os.path.exists(Recent_Files) == False:
        shutil.copy(os.path.expanduser('~').replace('\\','/') + '/.nuke/recent_files', recentFilesPath)
        file = open(Recent_Files)
        f = file.readlines()
        f.reverse()
        #print f
        file.close()
        file = open(Recent_Files, "w")
        file.writelines(f)
        file.close()

def addToRecentFiles(nkFile):
    createFolder()
    file = open(Recent_Files, "r")
    f = file.readlines()
    file.close()
    for i in f:
        if i == "%s\n" % nkFile:
            f.remove(i)
    f.append("%s\n" % nkFile)
    file = open(Recent_Files, "w")
    file.writelines(f)
    file.close()

def readRecentFiles(searchStr):
    createFolder()
    file = open(Recent_Files)
    f = file.readlines()
    file.close()
    fileList = []
    if ws.getSetting("maxRecentFiles") == "None":
        for i in f:
            j = i.replace("\n", "")
            if j.split("/")[-1].find(searchStr) != -1:
                fileList.append(j)
    else:
        number = min(int(ws.getSetting("maxRecentFiles")), len(f))
        for i in f[0:number]:
            j = i.replace("\n", "")
            if j.split("/")[-1].find(searchStr) != -1:
                fileList.append(j)
    fileList.reverse()
    #print fileList
    length = len(fileList)
    #print length
    if length > 0:
        pageNum = length/6
        if length%6 > 0:
            pageNum = pageNum + 1
        #print pageNum
        pageList = [[] for i in range(pageNum)]
        for i in range(pageNum-1):
            for j in range(6):
                pageList[i].append(fileList[i * 6 + j])
        for j in range(length - (pageNum-1) * 6):
            pageList[pageNum-1].append(fileList[(pageNum-1) * 6 + j])
        #print pageList
    else:
        pageList = []
    return pageList


#createFolder()
#addToRecentFiles("aaa.nk")
#print readRecentFiles("aab")