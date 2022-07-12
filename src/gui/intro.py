from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel

class IntroPage(QWidget):
    def __init__(self):
        super().__init__()
        self.wrapper = QHBoxLayout()
        self.main = QVBoxLayout()

        self.wrapper.addStretch()
        self.main.addStretch()

        self.img_label = QLabel()
        self.pixmap = QPixmap("../assets/safe-icon.png").scaledToWidth(100, Qt.SmoothTransformation)
        self.img_label.setPixmap(self.pixmap)
        self.img_label.setAlignment(Qt.AlignCenter)
        self.img_label.setStyleSheet("border-radius: 20px;")
        self.main.addWidget(self.img_label)

        self.main.addSpacing(10)

        self.create_btn = QPushButton(text="Create a new safe")
        self.create_btn.setStyleSheet("font-size: 21px; padding: 15px; font-weight: bold;")
        self.main.addWidget(self.create_btn)

        self.load_btn = QPushButton(text="Load safe")
        self.main.addWidget(self.load_btn)

        self.main.addStretch()

        self.wrapper.addLayout(self.main)

        self.wrapper.addStretch()

        self.setLayout(self.wrapper)