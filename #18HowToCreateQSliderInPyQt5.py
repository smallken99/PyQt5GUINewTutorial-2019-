from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QSlider,QPushButton,QLineEdit,QSplitter,QFrame,QMainWindow,QWidget,QSizeGrip,QGroupBox,QWidget,QHBoxLayout,QVBoxLayout,QLabel,QRadioButton

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 QSlider"
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
        self.setStyleSheet('background-color:green')
        hbox = QHBoxLayout()

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.changedValue)
        self.label = QLabel("0")
        self.label.setFont(QtGui.QFont("Sanserif",14))


        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)

        self.setLayout(hbox)
        self.show()

    def changedValue(self):
        size = self.slider.value()
        self.label.setText(str(size))

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
