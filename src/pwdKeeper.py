import sys

from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QStackedLayout
from PyQt5.QtWidgets import QWidget

from gui.intro import IntroPage
from gui.create import CreatePasswordPage
from gui.login import LoginPage
from gui.main import MainPage

from control.controller import Controller

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowIcon(QIcon("../assets/lockie.png"))
        self.setWindowTitle("pwdKeeper")
        self.resize(1024, 576)
        self.setMinimumSize(720, 320)

        self.stacked = QStackedLayout()

        self.intro_page = IntroPage()
        self.stacked.addWidget(self.intro_page)

        self.create_page = CreatePasswordPage()
        self.stacked.addWidget(self.create_page)

        self.login_page = LoginPage()
        self.stacked.addWidget(self.login_page)

        self.main_page = MainPage()
        self.stacked.addWidget(self.main_page)

        self.stacked.setCurrentIndex(3)
    
        self.setLayout(self.stacked)

        self.move(app.desktop().screen().rect().center() - self.rect().center())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    c = Controller(window)

    sys.exit(app.exec())