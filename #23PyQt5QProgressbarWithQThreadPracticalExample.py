from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QDialog,QPushButton,QProgressBar,QVBoxLayout

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap
from PyQt5.QtCore import Qt,QThread, pyqtSignal
from random import randint
import time

class MyTread(QThread):
    change_value = pyqtSignal(int)

    def run(self):
        cnt = 0
        while cnt < 100:
            cnt+=1
            time.sleep(0.3)
            self.change_value.emit(cnt)


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 QLCDNumber"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 100
        self.iconName = "icon.png"
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.initUI()
        self.show()

    def initUI(self):
        vbox = QVBoxLayout()
        self.progressbar = QProgressBar()
        self.progressbar.setMaximum(100)
        self.progressbar.setStyleSheet('QProgressBar {border: 2px solid grey; border-radius: 8px; padding: 1px}'
                                       "QProgressBar::chunk {background:green}")
        # self.progressbar.setOrientation(Qt.Vertical)
        self.progressbar.setTextVisible(False)

        vbox.addWidget(self.progressbar)


        self.button = QPushButton("Run Progressbar")
        self.button.clicked.connect(self.setProgressBar)
        self.button.setStyleSheet("background-color:yellow")
        vbox.addWidget(self.button)

        self.setLayout(vbox)
    def setProgressBar(self):
        self.thread = MyTread()
        self.thread.change_value.connect(self.setProgressVal)
        self.thread.start()
        
    def setProgressVal(self,val):
        self.progressbar.setValue(val)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
