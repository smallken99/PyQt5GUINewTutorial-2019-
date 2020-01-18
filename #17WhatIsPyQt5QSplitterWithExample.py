from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QLineEdit,QSplitter,QFrame,QMainWindow,QWidget,QSizeGrip,QGroupBox,QWidget,QHBoxLayout,QVBoxLayout,QLabel,QRadioButton

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Splitters"
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

        hbox = QHBoxLayout()
        left = QFrame()
        left.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)

        lineedit = QLineEdit()
        lineedit.setStyleSheet('background-color:green')

        splitter1.addWidget(left)
        splitter1.addWidget(lineedit)
        splitter1.setSizes([200,200])
        splitter1.setStyleSheet('background-color:red')

        splitter2  = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        splitter2.setStyleSheet('background-color:yellow')

        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())