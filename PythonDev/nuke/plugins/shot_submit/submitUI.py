import os
import nuke
import shlex
import threading
import subprocess
import PySide.QtGui as QtGui
from Widgets.submit.hqueueWidget import HQueueWidget


def async(fn):
    """Run *fn* asynchronously."""
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
    return wrapper


class ShotSubmitUI(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setLayout(QtGui.QVBoxLayout())
        renderBox = QtGui.QGroupBox('Render Set')
        renderBoxLayout = QtGui.QGridLayout()
        renderBox.setLayout(renderBoxLayout)
        self.layout().addWidget(renderBox)
        renderBoxLayout.addWidget(QtGui.QLabel('Filename:'), 0, 0)
        self.fileTextBox = QtGui.QLineEdit()
        self.fileTextBox.setReadOnly(True)
        try:
            filename = nuke.scriptName()
        except RuntimeError:
            filename = ''
        self.fileTextBox.setText(filename)
        browseButton = QtGui.QToolButton()
        browseButton.setText('...')
        browseButton.clicked.connect(self.openFileBrowser)
        renderBoxLayout.addWidget(self.fileTextBox, 0, 1)
        renderBoxLayout.addWidget(browseButton, 0, 2)
        renderBoxLayout.addWidget(QtGui.QLabel('Frame Range:'), 1, 0)
        self.frameBox = QtGui.QLineEdit()
        renderBoxLayout.addWidget(self.frameBox, 1, 1)
        renderBoxLayout.addWidget(QtGui.QLabel('Frame Step:'), 2, 0)
        self.frameStepBox = QtGui.QLineEdit()
        renderBoxLayout.addWidget(self.frameStepBox, 2, 1)
        renderBoxLayout.addWidget(QtGui.QLabel('Write Node:'), 3, 0)
        self.writeNodeBox = QtGui.QComboBox()
        self.populateWriteNodes()
        renderBoxLayout.addWidget(self.writeNodeBox, 3, 1)
        self.jobWidget = HQueueWidget('Nuke')
        self.layout().addWidget(self.jobWidget)
        self.jobWidget.splitmodeDrop.setCurrentIndex(0)
        self.jobWidget.splitmodeDrop.setEnabled(False)
        self.jobWidget.poolDrop.setCurrentIndex(2)
        self.jobWidget.progLineEdit.setEnabled(False)
        hlayout = QtGui.QHBoxLayout()
        submitButton = QtGui.QPushButton('Submit')
        submitButton.clicked.connect(self.submitRender)
        hlayout.addWidget(submitButton)
        hlayout.addItem(QtGui.QSpacerItem(10, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.layout().addLayout(hlayout)
        self.layout().addItem(QtGui.QSpacerItem(10, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding))

    def populateWriteNodes(self):
        writeNodes = nuke.allNodes('Write')
        deliveryNodes = nuke.allNodes('delivery')
        for node in deliveryNodes:
            self.writeNodeBox.addItem(node.name())
        for node in writeNodes:
            self.writeNodeBox.addItem(node.name())

    def openFileBrowser(self):
        dialog = QtGui.QFileDialog()
        filename, fileType = dialog.getOpenFileName(self, "Select File",
                                                    os.path.dirname(self.fileTextBox.text()),
                                                    options=QtGui.QFileDialog.DontUseNativeDialog)
        self.fileTextBox.setText(str(filename))

    def getRendererParams(self):
        renderParams = ''
        if str(self.frameBox.text()) is not '':
            frames = str(self.frameBox.text()).replace('-', ',').strip()
            # remove any whitespaces in the string and replace '-' with ','
            frames = ''.join(frames.replace('-',',').split())
        else:
            frames = '%s,%s' % (nuke.tcl('frames first'), nuke.tcl('frames last'))
        if str(self.frameStepBox.text()) is not '':
            frames = '%sx%s' % (frames, str(self.frameStepBox.text()))
        renderParams = '-F %s' % frames
        renderParams = '%s -X %s' % (renderParams, str(self.writeNodeBox.currentText()))
        return renderParams

    @async
    def submitLocalRender(self, cmd):
        logFile = self.jobWidget.getLogFileName()
        args = shlex.split(cmd)
        with open(logFile, 'w') as f:
            subprocess.call(args, stdout=f, stderr=f)

    def submitRender(self):
        filename = str(self.fileTextBox.text())
        nuke.scriptSave()
        if filename.endswith('.autosave'):
            nuke.message('Cannot submit .autosave file for render! Please save and try again.')
            return
        if filename is '' or not os.path.exists(filename):
            nuke.message('Please select a valid file to render!')
            return
        fileDir, fname = os.path.split(filename)
        jobName = 'Nuke - %s' % fname
        renderer = self.jobWidget.getRenderer('Nuke')
        splitMode = self.jobWidget.getSplitMode()
        local = self.jobWidget.localCheckbox.isChecked()
        pool = self.jobWidget.getClientPools()
        if pool == 'Linux Farm':
            pool = ''
        slackUser = self.jobWidget.getSlackUser()
        rendererParams = self.getRendererParams()
        priority = self.jobWidget.getPriority()
        dependent = self.jobWidget.getDependentJob()
        cmd = '%s %s %s' % (renderer, rendererParams, filename)
        hq_server = self.jobWidget.getHQProxy()
        if local:
            newCmd = cmd.split(';')[-1]
            self.submitLocalRender(newCmd)
            nuke.message('Local render started. \nCommand: %s' % newCmd)
        else:
            jobIds = self.jobWidget.submitNoChunk(hq_server, jobName, cmd, priority, 0,
                                                  pool, False, slackUser, dependent)
            nuke.message('Job Submission Successful. Job Ids = {0}'.format(jobIds))
