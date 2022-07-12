from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QDialog

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QComboBox


class ServiceDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.main = QVBoxLayout()
        self.main.setContentsMargins(20,20,20,20)
        self.main.setSpacing(20)
        
        self.label = QLabel(text="Add new account")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-weight: bold; font-size: 18px;")
        self.main.addWidget(self.label)

        
        self.form = QFormLayout()
        self.form.setSpacing(3)
        self.combox_label = QLabel(text="Service:")
        self.combox = QComboBox()
        self.combox.setPlaceholderText("Select a service")
        self.combox.setEditable(True)
        self.combox.setFixedWidth(300)
        self.form.addRow(self.combox_label, self.combox)
        self.username_label = QLabel(text="Username:")
        self.username_entry = QLineEdit()
        self.username_entry.setFixedWidth(350)
        self.form.addRow(self.username_label, self.username_entry)
        self.password_label = QLabel(text="Password:")
        self.password_entry = QLineEdit()
        self.password_entry.setFixedWidth(350)
        self.form.addRow(self.password_label, self.password_entry)
        self.main.addLayout(self.form)
        
        self.add_btn = QPushButton(text="Add account")
        self.main.addWidget(self.add_btn)
        
        self.main.addStretch()
        self.setLayout(self.main)
        
        self.setFixedSize(self.sizeHint())