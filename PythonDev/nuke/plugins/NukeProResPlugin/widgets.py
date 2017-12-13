__author__ = 'Natasha'
import os
import PySide.QtGui as QtGui

class FileBrowseWidget(QtGui.QWidget):
    '''
    Creates a widget that contains a label and a file browser
    '''
    def __init__(self, labelName, fileName, outfile):
        '''
        Creates the elements of the widget.
        :param labelName: Name of the label
        '''
        super(FileBrowseWidget, self).__init__()
        self.layout = QtGui.QGridLayout()
        self.setLayout(self.layout)
        hLayout = QtGui.QHBoxLayout()
        fileLabel = QtGui.QLabel(labelName)
        hLayout.addWidget(fileLabel)
        self.fileEdit = QtGui.QLineEdit(fileName)
        self.fileEdit.setReadOnly(True)
        self.fileEdit.setToolTip('Click to select a file')
        self.saveFilePath = outfile
        hLayout.addWidget(self.fileEdit)
        self.layout.addLayout(hLayout,1,0)

    def addOpenFileDialogEvent(self):
        self.fileEdit.mousePressEvent = self.openFileDialog

    def addSaveFileDialogEvent(self):
        self.fileEdit.mousePressEvent = self.saveFileDialog

    def openFileDialog(self, event):
        '''
        Opens a file browser when the text box is clicked.
        :param event: Event triggered when the text box is clicked.
        :return:
        '''
        dialog = QtGui.QFileDialog()
        filename, fileType = dialog.getOpenFileName(self, "Select File",
            os.path.dirname(self.fileEdit.text()), options= QtGui.QFileDialog.DontUseNativeDialog)
        self.fileEdit.setText(str(filename))

    def saveFileDialog(self, event):
        '''
        Opens a file browser when the text box is clicked.
        :param event: Event triggered when the text box is clicked.
        :return:
        '''
        dialog = QtGui.QFileDialog()
        filename, fileType = dialog.getSaveFileName(self, "Save File",
            self.saveFilePath, options= QtGui.QFileDialog.DontUseNativeDialog)
        if not str(filename).endswith('.mov'):
            filename = str(filename) + '.mov'
        self.fileEdit.setText(str(filename))

    def getFilePath(self):
        '''
        :return: The file selected by the user.
        '''
        return self.fileEdit.text()

    def setFilePath(self, filename):
        '''
        :param filename: The text box is set with this filename
        '''
        filename = str(filename)
        newFilename = filename.split('/')[-1].split('.')[0]
        if self.saveFilePath == '':
            self.saveFilePath = os.path.dirname(filename)
        newFilePath = '%s/%s.mov' % (os.path.dirname(self.saveFilePath), newFilename)
        self.fileEdit.setText(newFilePath)
