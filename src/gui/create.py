from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QProgressBar

from .bacctointro import BackWidget

class CreatePasswordPage(QWidget):
    def __init__(self):
        super().__init__()

        self.wrapper = QHBoxLayout()
        self.main = QVBoxLayout()
        self.form = QFormLayout()

        self.wrapper.addStretch()
        self.main.addStretch()
        
        self.main.addSpacing(30)

        self.label = QLabel(text="Create a password for the new vault")
        self.label.setStyleSheet("font-size: 40px;")
        self.main.addWidget(self.label)
        
        self.path_label = QLabel(text="...")
        self.path_label.setStyleSheet("color: gray;")
        self.main.addWidget(self.path_label, alignment=Qt.AlignCenter)

        self.main.addSpacing(30)

        self.pwd_label = QLabel(text="Enter a password:")
        self.pwd_entry = QLineEdit()
        self.pwd_entry.setMaximumWidth(250)
        self.pwd_entry.setEchoMode(QLineEdit.Password)
        self.form.addRow(self.pwd_label, self.pwd_entry)

        self.pwd2_label = QLabel(text="Repeat the password:")
        self.pwd2_entry = QLineEdit()
        self.pwd2_entry.setMaximumWidth(250)
        self.pwd2_entry.setEchoMode(QLineEdit.Password)
        self.form.addRow(self.pwd2_label, self.pwd2_entry)

        self.form.setFormAlignment(Qt.AlignCenter)
        self.main.addLayout(self.form)

        self.main.addSpacing(8)

        self.enter_btn = QPushButton(text="Enter!")
        self.enter_btn.setMinimumWidth(250)
        self.enter_btn.setDisabled(True)
        self.main.addWidget(self.enter_btn, alignment=Qt.AlignCenter)
        
        self.crack_label = QLabel()
        self.crack_label.setStyleSheet("color: grey;")
        self.main.addWidget(self.crack_label, alignment=Qt.AlignCenter)
        
        self.main.addStretch()
        
        self.bacc = BackWidget()
        self.main.addWidget(self.bacc, alignment=Qt.AlignCenter)

        self.wrapper.addLayout(self.main)
        self.wrapper.addStretch()
        self.setLayout(self.wrapper)