from PyQt5.QtWidgets import QApplication,QStackedWidget,QPushButton,QDialog,QGroupBox,QComboBox,QCheckBox,QWidget,QVBoxLayout,QLabel,QLineEdit,QDialogButtonBox,QTabWidget
import sys
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui


class StackWidget(QDialog):
    def __init__(self):
        super().__init__()
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle('PyQt5 Tab Widget')
        self.setWindowIcon(QIcon("icon.png"))
        self.StackedWidget()
        self.show()

    def StackedWidget(self):
        vbox = QVBoxLayout()

        self.stackWidget = QStackedWidget()
        vbox.addWidget(self.stackWidget)

        for x in range(0,8):
            label = QLabel("Stacked Child " + str(x))
            label.setFont(QtGui.QFont("Sanserif",15))
            label.setStyleSheet('color:red')

            self.stackWidget.addWidget(label)

            self.button = QPushButton("Stack " + str(x))
            self.button.setStyleSheet("background-color:green")
            self.button.page = x
            self.button.clicked.connect(self.btn_clicked)

            vbox.addWidget(self.button)
        self.setLayout(vbox)

    def btn_clicked(self):
        self.button = self.sender()
        self.stackWidget.setCurrentIndex(self.button.page)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    stackwidget = StackWidget()
    stackwidget.show()
    sys.exit(App.exec())