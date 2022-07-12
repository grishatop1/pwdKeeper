from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel

class MainPage(QWidget):
    def __init__(self):
        super().__init__()

        self.main = QVBoxLayout()

        self.toolbar = ToolbarLayout()
        self.main.addLayout(self.toolbar)

        self.setLayout(self.main)


class ToolbarLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.lock_label = QLabel(text="Fernet Encryption")
        self.lock_pixmap = QPixmap("../assets/lock.png").scaledToWidth(32, Qt.SmoothTransformation)
        self.lock_label.setPixmap(self.lock_pixmap)

        self.addWidget(self.lock_label)