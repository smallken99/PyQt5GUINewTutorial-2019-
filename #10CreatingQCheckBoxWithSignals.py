from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QLabel,QDialog,QVBoxLayout,QGroupBox,QCheckBox,QHBoxLayout

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap
class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Check Box"
        self.left = 300
        self.top = 200
        self.width = 400
        self.height = 100
        self.iconName = "icon.png"
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.CreatecCheckBox()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupbox)
        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif",13))
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.show()


    def CreatecCheckBox(self):
        self.groupbox = QGroupBox("What is your favorite programming language?")
        self.groupbox.setFont(QtGui.QFont("Sanserif",13))
        hboxlayout = QHBoxLayout()

        self.check1 = QCheckBox("Python")
        self.check1.setIcon(QtGui.QIcon("python.png"))
        self.check1.setIconSize(QtCore.QSize(40,40))
        self.check1.setFont(QtGui.QFont("Sanserif",13))
        self.check1.toggled.connect(self.onCheckBox_Toogled)
        hboxlayout.addWidget(self.check1)

        self.check2 = QCheckBox("Java")
        self.check2.setIcon(QtGui.QIcon("java.png"))
        self.check2.setIconSize(QtCore.QSize(40,40))
        self.check2.setFont(QtGui.QFont("Sanserif",13))
        self.check2.toggled.connect(self.onCheckBox_Toogled)
        hboxlayout.addWidget(self.check2)

        self.check3 = QCheckBox("PHP")
        self.check3.setIcon(QtGui.QIcon("php.png"))
        self.check3.setIconSize(QtCore.QSize(40,40))
        self.check3.setFont(QtGui.QFont("Sanserif",13))
        self.check3.toggled.connect(self.onCheckBox_Toogled)
        hboxlayout.addWidget(self.check3)

        self.groupbox.setLayout(hboxlayout)

    def onCheckBox_Toogled(self):
        if self.check1.isChecked():
            self.label.setText("You have selected " + self.check1.text())
        elif self.check2.isChecked():
            self.label.setText("You have selected " + self.check2.text())
        elif self.check3.isChecked():
            self.label.setText("You have selected " + self.check3.text())
        else:
            self.label.setText("")
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())