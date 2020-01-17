from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QPushButton,QWidget,QLineEdit,QHBoxLayout,QLabel

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Line Edit"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "icon.png"
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        hqbox = QHBoxLayout()
        self.lineedit = QLineEdit(self)
        self.lineedit.setFont(QtGui.QFont("Sanserif",15))
        self.lineedit.returnPressed.connect(self.onPressed)
        hqbox.addWidget(self.lineedit)
        self.label = QLabel(self)
        self.label.setFont((QtGui.QFont("Sanserif",15)))

        hqbox.addWidget(self.label)
        self.setLayout(hqbox)
        self.show()

    def onPressed(self):
        self.label.setText(self.lineedit.text())
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())