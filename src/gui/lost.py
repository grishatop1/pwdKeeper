from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QProgressBar

class LostPage(QWidget):
    def __init__(self):
        super().__init__()
        
        self.main = QVBoxLayout()
        self.main.setAlignment(Qt.AlignCenter)
        
        self.title = QLabel("Oh snap! Can't locate your pwdKeeper file!")
        self.title.setStyleSheet("font-size: 40px; font-weight: bold;")
        self.main.addWidget(self.title)
        
        self.path = QLabel("/home/... is missing!")
        self.path.setAlignment(Qt.AlignCenter)
        self.main.addWidget(self.path)
        
        self.btns_layout = QHBoxLayout()
        self.locate_btn = QPushButton("Relocate")
        self.locate_btn.setMaximumWidth(200)
        self.btns_layout.addWidget(self.locate_btn)
        self.load_btn = QPushButton("Load from backup")
        self.load_btn.setMaximumWidth(200)
        self.btns_layout.addWidget(self.load_btn)
        self.idc_btn = QPushButton("I don't care")
        self.idc_btn.setMaximumWidth(200)
        self.idc_btn.setStyleSheet("color: red;")
        self.btns_layout.addWidget(self.idc_btn)
        
        self.main.addSpacing(20)
        
        self.main.addLayout(self.btns_layout)
        
        self.setLayout(self.main)
