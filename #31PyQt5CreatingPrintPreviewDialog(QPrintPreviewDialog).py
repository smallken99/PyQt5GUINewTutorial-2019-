from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QAction,QMainWindow,QTextEdit,QFontDialog,QColorDialog

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5.QtGui import  QIcon
from PyQt5.QtCore import Qt
from random import randint
from PyQt5.QtPrintSupport import QPrinter,QPrintDialog,QPrintPreviewDialog


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 QPrintPreviewDialog"
        self.left = 500
        self.top = 200
        self.width = 500
        self.height = 400
        self.iconName = "icon.png"

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createEditor()
        self.CreateMent()
        self.show()

    def CreateMent(self):
        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu("File")
        editMenu = mainMenu.addMenu("Edit")
        viewMenu = mainMenu.addMenu("View")
        helpMenu = mainMenu.addMenu("Help")

        printAction = QAction(QIcon("print.png"),"Print",self)
        printAction.triggered.connect(self.printDialog)
        fileMenu.addAction(printAction)

        printPreviewAction = QAction(QIcon("preview.png"),"Preview",self)
        printPreviewAction.triggered.connect(self.printPreviewDialog)
        fileMenu.addAction(printPreviewAction)

        saveAction = QAction(QIcon("save.png"),'Save', self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)

        exitAction = QAction(QIcon("exit.png"),'Exit', self)
        exitAction.setShortcut("Ctrl+E")
        exitAction.triggered.connect(self.exitWindow)
        fileMenu.addAction(exitAction)

        copyAction = QAction(QIcon("copy.png"),'Copy', self)
        copyAction.setShortcut("Ctrl+C")
        editMenu.addAction(copyAction)

        cutAction = QAction(QIcon("cut.png"),'Cut', self)
        cutAction.setShortcut("Ctrl+X")
        editMenu.addAction(cutAction)

        pasteAction = QAction(QIcon("Paste.png"),'Paste', self)
        pasteAction.setShortcut("Ctrl+V")
        editMenu.addAction(pasteAction)

        fontAction = QAction(QIcon('font.png'),'Font',self)
        fontAction.setShortcut("Ctrl+F")
        fontAction.triggered.connect(self.fontDialog)
        viewMenu.addAction(fontAction)

        colorAction = QAction(QIcon("color.png"),"Color",self)
        colorAction.triggered.connect(self.colorDialog)
        viewMenu.addAction(colorAction)

        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(copyAction)
        toolbar.addAction(cutAction)
        toolbar.addAction(pasteAction)
        toolbar.addAction(saveAction)
        toolbar.addAction(exitAction)
        toolbar.addAction(fontAction)
        toolbar.addAction(colorAction)
        toolbar.addAction(printAction)
        toolbar.addAction(printPreviewAction)

    def exitWindow(self):
        self.close()

    def createEditor(self):
        self.textedit = QTextEdit(self)
        self.setCentralWidget(self.textedit)
        
    def fontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textedit.setFont(font)
    def colorDialog(self):
        color = QColorDialog.getColor()
        self.textedit.setTextColor(color)
    def printDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer,self)
        if dialog.exec_() == QPrintDialog.accepted:
            self.textedit.print_(printer)

    def printPreviewDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer,self)
        previewDialog.paintRequested.connect(self.printPreview)
        previewDialog.exec()

    def printPreview(self,printer):
        self.textedit.print_(printer)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
