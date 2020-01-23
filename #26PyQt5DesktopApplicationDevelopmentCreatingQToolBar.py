from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QAction,QMainWindow

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5.QtGui import  QIcon
from PyQt5.QtCore import Qt
from random import randint


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 QToolBar"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "icon.png"

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateMent()
        self.show()

    def CreateMent(self):
        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu("File")
        editMenu = mainMenu.addMenu("Edit")
        viewMenu = mainMenu.addMenu("View")
        helpMenu = mainMenu.addMenu("Help")

        copyAction = QAction(QIcon("copy.png"),'Copy', self)
        copyAction.setShortcut("Ctrl+C")
        fileMenu.addAction(copyAction)

        cutAction = QAction(QIcon("cut.png"),'Cut', self)
        cutAction.setShortcut("Ctrl+X")
        fileMenu.addAction(cutAction)

        saveAction = QAction(QIcon("save.png"),'Save', self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)

        exitAction = QAction(QIcon("exit.png"),'Exit', self)
        exitAction.setShortcut("Ctrl+E")
        exitAction.triggered.connect(self.exitWindow)
        editMenu.addAction(exitAction)

        pasteAction = QAction(QIcon("Paste.png"),'Paste', self)
        pasteAction.setShortcut("Ctrl+V")
        editMenu.addAction(pasteAction)

        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(copyAction)
        toolbar.addAction(cutAction)
        toolbar.addAction(pasteAction)
        toolbar.addAction(saveAction)
        toolbar.addAction(exitAction)

    def exitWindow(self):
        self.close()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
