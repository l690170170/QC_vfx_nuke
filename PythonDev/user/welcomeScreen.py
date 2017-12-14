# -*- coding: utf-8 -*-
# __author__ = 'XingHuan'
# 2017/2/28

from PySide.QtGui import *
from PySide.QtCore import *
import sys
import os
import welcome_path as wp
import welcome_helper as wh
import welcome_setting as ws

inNuke = True
if inNuke == True:
    import nuke

Home_Path = wp.Home_Path
Global_Icon_Path = "%s/icons" % Home_Path


VER = "v1.1"
AUTHOR = "XingHuan"
DATE = "2017/3/4"

FontSize = [5, 13, 10, 10]


class WelcomeScreen(QWidget):
    def __init__(self):
        super(WelcomeScreen, self).__init__()

        self.customWidth = 700
        self.customHeight = 600
        self.setFixedSize(self.customWidth, self.customHeight)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        if inNuke == False:
            self.setStyleSheet("background-color:rgb(50, 50, 50)")

        self.newCompLayout = QHBoxLayout()
        self.newCompIcon = IconLabel("new")
        self.newCompLabel = QCustomLabel("New Comp")
        self.connect(self.newCompLabel, SIGNAL('labelClicked()'), self.newComp)
        self.newCompLayout.addWidget(self.newCompIcon)
        self.newCompLayout.addSpacing(15)
        self.newCompLayout.addWidget(self.newCompLabel)
        self.newCompLayout.setAlignment(Qt.AlignLeft)

        self.openCompLayout = QHBoxLayout()
        self.openCompIcon = IconLabel("open")
        self.openCompLabel = QCustomLabel("Open Comp")
        self.connect(self.openCompLabel, SIGNAL('labelClicked()'), self.openComp)
        self.openCompLayout.addWidget(self.openCompIcon)
        self.openCompLayout.addSpacing(15)
        self.openCompLayout.addWidget(self.openCompLabel)
        self.openCompLayout.setAlignment(Qt.AlignLeft)

        self.settingLayout = QHBoxLayout()
        self.settingIcon = IconLabel("setting")
        self.settingLabel = QCustomLabel("Setting")
        self.connect(self.settingLabel, SIGNAL('labelClicked()'), self.showSetting)
        self.settingLayout.addWidget(self.settingIcon)
        self.settingLayout.addSpacing(15)
        self.settingLayout.addWidget(self.settingLabel)
        self.settingLayout.setAlignment(Qt.AlignLeft)

        self.aboutLayout = QHBoxLayout()
        self.aboutIcon = IconLabel("about")
        self.aboutLabel = QCustomLabel("About...")
        self.connect(self.aboutLabel, SIGNAL('labelClicked()'), self.showAbout)
        self.aboutLayout.addWidget(self.aboutIcon)
        self.aboutLayout.addSpacing(15)
        self.aboutLayout.addWidget(self.aboutLabel)
        self.aboutLayout.setAlignment(Qt.AlignLeft)

        self.leftLayout = QVBoxLayout()
        self.leftLayout.addLayout(self.newCompLayout)
        self.leftLayout.addLayout(self.openCompLayout)
        self.leftLayout.addLayout(self.settingLayout)
        self.leftLayout.addLayout(self.aboutLayout)
        self.leftLayout.addStretch()

        self.openRecentLabelLayout = QHBoxLayout()
        self.openRecentLabel = QLabel("Open Recent")
        self.openRecentLabel.setFont(QFont("Arial", FontSize[1]))
        self.openRecentLabel.setStyleSheet("color:rgb(180, 180, 180)")
        self.openRecentLabelLayout.addWidget(self.openRecentLabel)
        self.openRecentLabelLayout.addStretch()

        self.searchLabel = QLabel("Search")
        self.searchLabel.setFont(QFont("Arial", FontSize[2]))
        self.searchLabel.setStyleSheet("color:rgb(180, 180, 180)")
        self.searchLineEdit = QLineEdit()
        self.searchLineEdit.textChanged.connect(self.buildRecentList)
        self.searchLineEdit.setStyleSheet("color:rgb(180, 180, 180); padding:2px 2px 2px 20px; background-image:url(%s/search.png); background-color:rgb(50, 50, 50); background-position:left; background-repeat:no-repeat" % Global_Icon_Path)
        self.searchLayout = QHBoxLayout()
        self.searchLayout.addSpacing(30)
        self.searchLayout.addWidget(self.searchLabel)
        self.searchLayout.addSpacing(10)
        self.searchLayout.addWidget(self.searchLineEdit)
        self.searchLayout.addStretch()

        self.recentWidget = QRecentWidget()
        self.connect(self.recentWidget, SIGNAL('open_Script()'), self.afterOpen)

        self.pageLayout = QHBoxLayout()
        self.previousLabelButton = QLabelButton("previous")
        self.nextLabelButton = QLabelButton("next")
        self.connect(self.previousLabelButton, SIGNAL('buttonClicked()'), self.previousPage)
        self.connect(self.nextLabelButton, SIGNAL('buttonClicked()'), self.nextPage)
        self.pageLabel = QLabel()
        self.pageLabel.setText("0/0")
        self.pageLabel.setFont(QFont("Arial", 10))
        self.pageLabel.setStyleSheet("color:rgb(180, 180, 180)")
        self.pageLayout.addSpacing(230)
        self.pageLayout.addWidget(self.previousLabelButton)
        self.pageLayout.addStretch()
        self.pageLayout.addWidget(self.pageLabel)
        self.pageLayout.addStretch()
        self.pageLayout.addWidget(self.nextLabelButton)
        self.pageLayout.addSpacing(70)

        self.rightLayout = QVBoxLayout()
        self.rightLayout.addSpacing(7)
        #self.rightLayout.setSpacing(0)
        self.rightLayout.addLayout(self.openRecentLabelLayout)
        self.rightLayout.addSpacing(7)
        self.rightLayout.addLayout(self.searchLayout)
        self.rightLayout.setSpacing(0)
        self.rightLayout.addWidget(self.recentWidget)
        self.rightLayout.addLayout(self.pageLayout)
        self.rightLayout.addStretch()
        self.rightLayout.setAlignment(Qt.AlignLeft)

        self.upLayout = QHBoxLayout()
        self.upLayout.addLayout(self.leftLayout)
        self.upLayout.addSpacing(100)
        self.upLayout.addLayout(self.rightLayout)


        self.settingLayout = QHBoxLayout()
        self.showAtStartCheck = QCheckBox("Show Welcome Screen at Startup")
        self.showAtStartCheck.setStyleSheet("color:rgb(180, 180, 180); font-family:Arial")
        self.showAtStartCheck.clicked.connect(self.showAtStartChange)
        self.closeButton = QPushButton("Close")
        self.closeButton.setStyleSheet("color:rgb(180, 180, 180); background-color:rgb(39, 92, 132); font-family:Arial")
        self.closeButton.clicked.connect(self.close)
        self.settingLayout.addWidget(self.showAtStartCheck)
        self.settingLayout.addStretch()
        self.settingLayout.addWidget(self.closeButton)

        self.masterLayout = QVBoxLayout()
        self.masterLayout.addSpacing(170)
        self.masterLayout.addLayout(self.upLayout)
        self.masterLayout.addLayout(self.settingLayout)
        self.setLayout(self.masterLayout)

        screenRes = QDesktopWidget().screenGeometry()
        self.move(QPoint(screenRes.width() / 2, screenRes.height() / 2) - QPoint((self.width() / 2), (self.height() / 2)))
        self.allPages = 1
        self.curentPage = 1
        wh.createFolder()
        ws.createSetting()
        self.updateSetting()
        self.buildRecentList()


    def paintEvent(self, QPaintEvent):
        super(WelcomeScreen, self).paintEvent(QPaintEvent)

        painter = QPainter(self)
        brush = QBrush(QColor(151, 46, 60))
        pen = QPen(QColor(0, 0, 0, 0))
        painter.setPen(pen)
        painter.setBrush(brush)
        self.rect = QRect(0, 0, self.customWidth, 150)
        painter.drawRect(self.rect)

        self.nukeIcon = QPixmap("%s/logo.png" % Global_Icon_Path).scaled(400, 200 , Qt.KeepAspectRatio)
        painter.drawPixmap(QPoint(0, 0), self.nukeIcon)

        painter.setPen(QPen(QColor(255, 255, 255)))
        painter.setFont(QFont("Arial", 10))
        text = "THE FOUNDRY"
        painter.drawText(QRect(self.customWidth-150, 120, self.customWidth, 40), Qt.AlignLeft, text)

        pen = QPen(QColor(35, 35, 35, 200))
        pen.setWidth(1)
        painter.setPen(pen)
        line = QLine(QPoint(240, 170), QPoint(240, 500))
        painter.drawLine(line)

    def updateSetting(self):
        showAtStart = ws.getSetting("showAtStart")
        if showAtStart == "True":
            self.showAtStartCheck.setChecked(True)
        else:
            self.showAtStartCheck.setChecked(False)

    def newComp(self):
        self.afterOpen()
        if inNuke == True:
            nuke.scriptNew()

    def openComp(self):
        self.afterOpen()
        if inNuke == True:
            try:
                nuke.scriptOpen("")
            except:
                print "not open"

    def showSetting(self):
        #print "setting"
        self.settingWidget = SettingWidget()
        self.settingWidget.show()

    def showAbout(self):
        #print "about..."
        self.aboutWidget = AboutWidget()
        self.aboutWidget.show()

    def afterOpen(self):
        #print "open"
        if ws.getSetting("closeAfterOpen") == "True":
            self.close()

    def buildRecentList(self):
        #print "build list"
        self.allPages = self.recentWidget.addRecentFiles(self.searchLineEdit.text(), self.curentPage)
        if self.allPages == 0:
            self.allPages = 1
        self.updatePage()
        self.update()

    def previousPage(self):
        #print "previous"
        if self.curentPage > 1:
            self.curentPage = self.curentPage - 1
        self.updatePage()
        self.buildRecentList()

    def nextPage(self):
        #print "next"
        if self.curentPage < self.allPages:
            self.curentPage = self.curentPage + 1
        self.updatePage()
        self.buildRecentList()

    def updatePage(self):
        self.pageLabel.setText("%s/%s" % (self.curentPage, self.allPages))
        self.update()

    def showAtStartChange(self):
        if self.showAtStartCheck.isChecked():
            ws.changeSetting("showAtStart", "True")
        else:
            ws.changeSetting("showAtStart", "False")


class QCustomLabel(QLabel):
    def __init__(self, name):
        super(QCustomLabel, self).__init__()

        self.text = name
        self.textFont = "Arial"
        self.textSize = FontSize[0]
        self.setText('<font color = #BAA0D4 size = %s face = %s>%s</font>' % (self.textSize, self.textFont, self.text))
        self.setToolTip(name)

    def enterEvent(self, event):
        self.setText('<font color = #FFC132 size = %s face = %s>%s</font>' % (self.textSize, self.textFont, self.text))

    def leaveEvent(self,event):
        self.setText('<font color = #BAA0D4 size = %s face = %s>%s</font>' % (self.textSize, self.textFont, self.text))

    def mousePressEvent(self, event):
        self.setText('<font color = #DFA112 size = %s face = %s>%s</font>' % (self.textSize, self.textFont, self.text))

    def mouseReleaseEvent(self,event):
        self.setText('<font color = #FFC132 size = %s face = %s>%s</font>' % (self.textSize, self.textFont, self.text))
        self.emit(SIGNAL('labelClicked()'))

class QRecentLabel(QLabel):
    def __init__(self):
        super(QRecentLabel, self).__init__()
        self.filePath = ""



    def addRecentFile(self, filePath):
        self.filePath = filePath
        self.textFont = "Arial"
        self.textSize = FontSize[0]
        if filePath != "":
            self.text = os.path.basename(filePath)
            self.setText('<font color = #BAA0D4 size = %s face = %s>%s</font>' % (self.textSize, self.textFont, self.text))
            self.setToolTip(filePath)
        else:
            self.text = ""
            self.setText('<font color = #BAA0D4 size = %s face = %s>%s</font>' % (self.textSize, self.textFont, self.text))

    def enterEvent(self, event):
        self.setText('<font color = #FFC132 size = %s face = %s>%s</font>' % (self.textSize, self.textFont, self.text))

    def leaveEvent(self,event):
        self.setText('<font color = #BAA0D4 size = %s face = %s>%s</font>' % (self.textSize, self.textFont, self.text))

    def mousePressEvent(self, event):
        self.setText('<font color = #DFA112 size = %s face = %s>%s</font>' % (self.textSize, self.textFont, self.text))

    def mouseReleaseEvent(self,event):
        self.setText('<font color = #FFC132 size = %s face = %s>%s</font>' % (self.textSize, self.textFont, self.text))
        self.emit(SIGNAL('openScript()'))
        if inNuke == True:
            try:
                nuke.scriptOpen(self.filePath)
            except:
                print "open error"

class IconLabel(QLabel):
    def __init__(self, name):
        super(IconLabel, self).__init__()

        path = "%s/%s.png" % (Global_Icon_Path, name)
        self.imageFile = path
        if name != "recent":
            self.setPixmap(QPixmap(self.imageFile).scaled(50, 50 , Qt.KeepAspectRatio))
        else:
            self.setPixmap(QPixmap(self.imageFile).scaled(35, 35, Qt.KeepAspectRatio))

class QRecentWidget(QWidget):
    def __init__(self):
        super(QRecentWidget, self).__init__()
        self.setFixedHeight(270)

        self.allPages = 1

        self.masterLayout = QVBoxLayout()
        self.masterLayout.setSpacing(0)
        self.recentLabelLayout = [QHBoxLayout() for i in range(6)]
        self.recentIcon = [IconLabel("recent") for i in range(6)]
        self.recentLabel = [QRecentLabel() for i in range(6)]

        for i in range(6):
            self.recentLabel[i].addRecentFile("")
            self.connect(self.recentLabel[i], SIGNAL('openScript()'), self.openScriptEmit)
            self.recentLabelLayout[i].setAlignment(Qt.AlignLeft)
            self.recentLabelLayout[i].addSpacing(15)
            self.recentLabelLayout[i].addWidget(self.recentIcon[i])
            self.recentLabelLayout[i].addSpacing(15)
            self.recentLabelLayout[i].addWidget(self.recentLabel[i])
            self.masterLayout.addLayout(self.recentLabelLayout[i])
            self.masterLayout.addSpacing(5)
        self.masterLayout.setAlignment(Qt.AlignTop)
        self.masterLayout.addStretch()
        self.setLayout(self.masterLayout)

    def addRecentFiles(self, searchStr, currentPage):
        filesList = wh.readRecentFiles(searchStr)
        self.allPages = len(filesList)
        #print filesList
        if len(filesList) > 0:
            currentPageFilesNum = len(filesList[currentPage-1])
            #print currentPageFilesNum
            for i in range(currentPageFilesNum):
                self.recentLabel[i].addRecentFile("%s" % filesList[currentPage-1][i])
                self.recentIcon[i].show()
            for i in range(currentPageFilesNum, 6):
                self.recentLabel[i].addRecentFile("")
                self.recentIcon[i].hide()
        else:
            for i in range(6):
                self.recentLabel[i].addRecentFile("")
                self.recentIcon[i].hide()
        return len(filesList)

    def openScriptEmit(self):
        self.emit(SIGNAL('open_Script()'))

class QLabelButton(QLabel):
    def __init__(self, name):
        super(QLabelButton, self).__init__()

        self.imageFile = '%s/%s.png' % (Global_Icon_Path, name)
        self.setPixmap(QPixmap(self.imageFile).scaled(20, 20))
        self.setStyleSheet("background-color: rgb(54, 54, 54, 0)")

    def enterEvent(self, event):
        self.setStyleSheet("background-color: rgb(80, 80, 80, 255)")

    def leaveEvent(self, event):
        self.setStyleSheet("background-color: rgb(54, 54, 54, 0)")

    def mousePressEvent(self, event):
        self.setStyleSheet("background-color: rgb(30, 30, 30, 255)")

    def mouseReleaseEvent(self, event):
        self.emit(SIGNAL('buttonClicked()'))
        self.setStyleSheet("background-color: rgb(80, 80, 80, 255)")

class AboutWidget(QWidget):
    def __init__(self):
        super(AboutWidget, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setFixedSize(270, 250)
        self.setWindowTitle("About")

        self.setStyleSheet("color: white; background-color: rgb(50, 50, 50)")
        aboutToolbox = QLabel()
        aboutToolbox.setPixmap(QPixmap("%s/aboutWS.png" % Global_Icon_Path).scaled(250, 100, Qt.KeepAspectRatio))
        aboutVer = QLabel(VER)
        aboutVer.setStyleSheet("font:20px Arial")
        aboutAuthor = QLabel("Author:%s" % AUTHOR)
        aboutAuthor.setAlignment(Qt.AlignRight)
        aboutAuthor.setStyleSheet("font:15px Arial")
        aboutDate = QLabel("Date:%s" % DATE)
        aboutDate.setAlignment(Qt.AlignRight)
        aboutDate.setStyleSheet("font:15px Arial")

        self.masterLayout = QVBoxLayout()
        self.masterLayout.addWidget(aboutToolbox)
        self.masterLayout.addWidget(aboutVer)
        self.masterLayout.addWidget(aboutAuthor)
        self.masterLayout.addWidget(aboutDate)
        self.setLayout(self.masterLayout)

        self.adjustSize()
        screenRes = QDesktopWidget().screenGeometry()
        #self.move(QPoint(screenRes.width()/2,screenRes.height()/2)-QPoint((self.width()/2),(self.height()/2)))
        self.move(QPoint(0, 0))

class SettingWidget(QWidget):
    def __init__(self):
        super(SettingWidget, self).__init__()

        self.setFixedSize(450, 300)
        self.setFont(QFont("Arial", FontSize[3]))
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.maxRecentFilesLayout = QHBoxLayout()
        self.maxRecentFilesLabel = QLabel("Show max recent files: ")
        self.maxRecentFilesLine = QLineEdit()
        self.maxRecentFilesLayout.addWidget(self.maxRecentFilesLabel)
        self.maxRecentFilesLayout.addWidget(self.maxRecentFilesLine)
        self.maxRecentFilesLayout.addStretch()
        self.maxRecentFilesLayout.setAlignment(Qt.AlignLeft)

        self.closeAfterOpenLayout = QHBoxLayout()
        self.closeAfterOpenLabel = QLabel("Close after open a script: ")
        self.closeAfterOpenCheck = QCheckBox()
        self.closeAfterOpenLayout.addWidget(self.closeAfterOpenLabel)
        self.closeAfterOpenLayout.addWidget(self.closeAfterOpenCheck)
        self.closeAfterOpenLayout.addStretch()
        self.closeAfterOpenLayout.setAlignment(Qt.AlignLeft)

        self.okCancelLayout = QHBoxLayout()
        self.okButton = QPushButton("Ok")
        self.okButton.clicked.connect(self.changeSetting)
        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.clicked.connect(self.close)
        self.okCancelLayout.addStretch()
        self.okCancelLayout.addWidget(self.okButton)
        self.okCancelLayout.addWidget(self.cancelButton)
        self.okCancelLayout.setAlignment(Qt.AlignRight)

        self.masterLayout = QVBoxLayout()
        self.masterLayout.addLayout(self.maxRecentFilesLayout)
        self.masterLayout.addLayout(self.closeAfterOpenLayout)
        self.masterLayout.addStretch()
        self.masterLayout.addLayout(self.okCancelLayout)

        self.setLayout(self.masterLayout)
        self.loadSetting()

        self.move(QPoint(0, 0))

    def loadSetting(self):
        maxRecentFiles = ws.getSetting("maxRecentFiles")
        closeAfterOpen = ws.getSetting("closeAfterOpen")
        self.maxRecentFilesLine.setText(maxRecentFiles)
        if closeAfterOpen == "True":
            self.closeAfterOpenCheck.setChecked(True)
        else:
            self.closeAfterOpenCheck.setChecked(False)

    def changeSetting(self):
        maxRecentFiles = self.maxRecentFilesLine.text()
        if self.closeAfterOpenCheck.isChecked():
            closeAfterOpen = "True"
        else:
            closeAfterOpen = "False"
        ws.changeSetting("maxRecentFiles", maxRecentFiles)
        ws.changeSetting("closeAfterOpen", closeAfterOpen)
        self.close()







welcomeScreen = WelcomeScreen()


if ws.getSetting("showAtStart") == "True":
    welcomeScreen.buildRecentList()
    welcomeScreen.show()

def main():
	welcomeScreen.buildRecentList()
	welcomeScreen.show()


