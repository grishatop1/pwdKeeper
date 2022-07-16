from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QProgressBar

class BackWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.main = QHBoxLayout()
        self.main.addStretch()
        self.btn = QPushButton(text="Back")
        self.main.addWidget(self.btn)
        
        self.setLayout(self.main)