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
        
        self.label = QLabel(text="pwdKeeper")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 50px; font-weight: bold;")
        self.main.addWidget(self.label)

        self.img_label = QLabel()
        self.pixmap = QPixmap("../assets/safe-icon.png").scaledToWidth(100, Qt.SmoothTransformation)
        self.img_label.setPixmap(self.pixmap)
        self.img_label.setAlignment(Qt.AlignCenter)
        self.img_label.setStyleSheet("border-radius: 20px;")
        self.main.addWidget(self.img_label)

        self.main.addSpacing(50)
        
        self.btns = QVBoxLayout()
        self.btns.setAlignment(Qt.AlignCenter)

        self.create_btn = QPushButton(text="Create a new safe")
        self.create_btn.setStyleSheet("font-size: 21px; padding: 15px;")
        self.create_btn.setMaximumWidth(250)
        self.btns.addWidget(self.create_btn)

        self.load_btn = QPushButton(text="Load safe")
        self.load_btn.setMaximumWidth(250)
        self.btns.addWidget(self.load_btn)
        
        self.main.addLayout(self.btns)
        
        self.main.addStretch()
        
        self.aes = QLabel(text="Heavy encryption is in use! Just make sure your safe password is strong enough.")
        self.aes.setStyleSheet("color: gray;")
        self.aes.setAlignment(Qt.AlignCenter)
        self.main.addWidget(self.aes)

        self.wrapper.addLayout(self.main)

        self.wrapper.addStretch()

        self.setLayout(self.wrapper)