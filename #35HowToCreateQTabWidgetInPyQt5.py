from PyQt5.QtWidgets import QApplication,QDialog,QGroupBox,QComboBox,QCheckBox,QWidget,QVBoxLayout,QLabel,QLineEdit,QDialogButtonBox,QTabWidget
import sys
from PyQt5.QtGui import QIcon



class Tab(QDialog):
    def __init__(self):
        super().__init__()
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle('PyQt5 Tab Widget')
        self.setWindowIcon(QIcon("icon.png"))

        vbox = QVBoxLayout()
        tabWidget = QTabWidget()

        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)

        tabWidget.addTab(TabContact(),"Contact Details")
        tabWidget.addTab(TabPersonDetails(), "Person Details")
        vbox.addWidget(tabWidget)
        vbox.addWidget(buttonbox)
        self.setLayout(vbox)


class TabContact(QWidget):
    def __init__(self):
        super().__init__()

        name = QLabel("Name: ")
        nameEdit = QLineEdit()

        phone = QLabel("Phone: ")
        phoneEdit = QLineEdit()


        email = QLabel("Email: ")
        emailEdit = QLineEdit()

        addr = QLabel("Address: ")
        addrEdit = QLineEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(name)
        vbox.addWidget(nameEdit)
        vbox.addWidget(phone)
        vbox.addWidget(phoneEdit)
        vbox.addWidget(email)
        vbox.addWidget(emailEdit)
        vbox.addWidget(addr)
        vbox.addWidget(addrEdit)

        self.setLayout(vbox)

class TabPersonDetails(QWidget):
    def __init__(self):
        super().__init__()

        groupbox = QGroupBox("Select Your Gender?")
        list = ['Mail', "Female"]

        combo = QComboBox()
        combo.addItems(list)

        vbox = QVBoxLayout()
        vbox.addWidget(combo)

        groupbox.setLayout(vbox)

        groupbox2 = QGroupBox('Select Your Favorite Programming Language?')
        python = QCheckBox("Python")
        cpp   = QCheckBox("C++")
        java  = QCheckBox("Java")
        csharp  = QCheckBox("C#")

        vboxp = QVBoxLayout()
        vboxp.addWidget(python)
        vboxp.addWidget(cpp)
        vboxp.addWidget(java)
        vboxp.addWidget(csharp)

        groupbox2.setLayout(vboxp)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(groupbox)
        mainLayout.addWidget(groupbox2)

        self.setLayout(mainLayout)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    tabdialog = Tab()
    tabdialog.show()
    sys.exit(App.exec())