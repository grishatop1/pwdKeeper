from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QDialog

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QComboBox

from data.services import services


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
        self.combox.addItems(services)
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
        
class EditTab(QDialog):
    def __init__(self, service, username, password):
        super().__init__()
        
        self.main = QVBoxLayout()
        self.main.setContentsMargins(20,20,20,20)
        self.main.setSpacing(20)
        
        self.label = QLabel(text="Edit account")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-weight: bold; font-size: 18px;")
        self.main.addWidget(self.label)

        
        self.form = QFormLayout()
        self.form.setSpacing(3)
        self.combox_label = QLabel(text="Service:")
        self.combox = QComboBox()
        self.combox.setCurrentText(service)
        self.combox.addItem(service)
        self.combox.setPlaceholderText("Select a service")
        self.combox.setEditable(True)
        self.combox.setFixedWidth(300)
        
        self.combox.addItems()
        
        self.form.addRow(self.combox_label, self.combox)
        self.username_label = QLabel(text="Username:")
        self.username_entry = QLineEdit()
        self.username_entry.setText(username)
        self.username_entry.setFixedWidth(350)
        self.form.addRow(self.username_label, self.username_entry)
        self.password_label = QLabel(text="Password:")
        self.password_entry = QLineEdit(self)
        self.password_entry.setText(password)
        self.password_entry.setFixedWidth(350)
        self.password_entry.setFocus()
        self.form.addRow(self.password_label, self.password_entry)
        self.main.addLayout(self.form)
        
        self.change_btn = QPushButton(text="Apply changes")
        self.main.addWidget(self.change_btn)
        
        self.main.addStretch()
        self.setLayout(self.main)
        
        self.setFixedSize(self.sizeHint())