from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QScrollArea,QFormLayout,QGroupBox,QSlider,QPushButton,QLineEdit,QSplitter,QFrame,QMainWindow,QWidget,QSizeGrip,QGroupBox,QWidget,QHBoxLayout,QVBoxLayout,QLabel,QRadioButton

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self, val):
        super().__init__()
        self.title = "PyQt5 QScroll Area"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "icon.png"

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        formLayout = QFormLayout()
        groupbox = QGroupBox("This is Group box")
        labelList = []
        buttonList = []

        for i in range(val):
            labelList.append(QLabel("Label"))
            buttonList.append(QPushButton("Click Me"))
            formLayout.addRow(labelList[i], buttonList[i])

        groupbox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupbox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)

        layout = QVBoxLayout()
        layout.addWidget(scroll)
        self.setLayout(layout)
        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window(20)
    sys.exit(App.exec())
