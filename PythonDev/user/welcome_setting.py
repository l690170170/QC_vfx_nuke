# -*- coding: utf-8 -*-
# __author__ = 'XingHuan'
# 2017/3/4
import os
import welcome_path as wp

Current_User = os.path.expanduser('~').replace('\\','/').split("/")[-1]
Setting_File = "%s/%s/setting" % (wp.Users_Path, Current_User)

DefaultSetting = ["showAtStart True\n", "maxRecentFiles None\n", "closeAfterOpen True\n"]

def createSetting():
    settingFilePath = "%s/%s" % (wp.Users_Path, Current_User)
    if os.path.exists(settingFilePath) == False:
        os.makedirs(settingFilePath)
    if os.path.exists(Setting_File) == False:
        f = DefaultSetting
        file = open(Setting_File, "w")
        file.writelines(f)
        file.close()

def changeSetting(name, value):
    file = open(Setting_File, "r")
    f = file.readlines()
    file.close()
    #print f
    newF = []
    for i in f:
        if i.find(name) == 0:
            temp = i.split(" ")
            temp[1] = "%s\n" % value
            j = " ".join(temp)
            newF.append(j)
        else:
            newF.append(i)
    file = open(Setting_File, "w")
    file.writelines(newF)
    file.close()
    #print newF

def getSetting(name):
    file = open(Setting_File, "r")
    f = file.readlines()
    file.close()
    #print f
    for i in f:
        if i.find(name) == 0:
            return i.split(" ")[1].replace("\n", "")


#createSetting()
#changeSetting("maxRecentFiles", "None")
#changeSetting("showAtStart", "True")
#changeSetting("closeAfterOpen", "True")
#changeSetting("closeAfterOpen", "False")
#print getSetting("showAtStart")