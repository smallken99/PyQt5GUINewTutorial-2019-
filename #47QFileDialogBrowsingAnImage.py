from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QDialog,QPushButton,QMainWindow,QLabel,QFileDialog,QVBoxLayout

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 QFileDialog"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "icon.png"
        self.InitUI()

    def InitUI(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()

        self.btn = QPushButton("Browse Image")
        self.btn.clicked.connect(self.browseImage)
        vbox.addWidget(self.btn)

        self.label = QLabel(self)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.show()

    def browseImage(self):
        fname = QFileDialog.getOpenFileName(self,'Open File','c\\','Image Files (*.jpg *.gif *.png)')
        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        self.label.setPixmap(QPixmap(pixmap))
        print(fname,imagePath)
        self.resize(pixmap.width(),pixmap.height())

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())