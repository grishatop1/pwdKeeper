from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QProgressBar

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()

        self.wrapper = QHBoxLayout()
        self.main = QVBoxLayout()
        self.form = QFormLayout()

        self.wrapper.addStretch()
        self.main.addStretch()

        self.label = QLabel(text="Enter the password for your safe")
        self.label.setStyleSheet("font-size: 40px;")
        self.main.addWidget(self.label)

        self.main.addSpacing(30)

        self.pwd_label = QLabel(text="Enter the password:")
        self.pwd_entry = QLineEdit()
        self.pwd_entry.setMaximumWidth(250)
        self.form.addRow(self.pwd_label, self.pwd_entry)

        self.form.setFormAlignment(Qt.AlignCenter)
        self.main.addLayout(self.form)

        self.main.addSpacing(8)

        self.enter_btn = QPushButton(text="Enter!")
        self.enter_btn.setMinimumWidth(250)
        self.main.addWidget(self.enter_btn, alignment=Qt.AlignCenter)

        self.main.addStretch()
        self.wrapper.addLayout(self.main)
        self.wrapper.addStretch()
        self.setLayout(self.wrapper)