from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QScrollArea

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit

from PyQt5.QtWidgets import QGraphicsDropShadowEffect

class MainPage(QWidget):
    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()

        self.toolbar = ToolbarLayout()
        self.main_layout.addLayout(self.toolbar)
        
        self.search = SearchLayout()
        self.main_layout.addLayout(self.search)
        
        self.main = MainLayout()
        self.main_layout.addLayout(self.main)

        self.setLayout(self.main_layout)
        
        
class MainLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        
        self.scroll = QScrollArea()
        self.w = QWidget()
        self.list = QVBoxLayout()
        
        self.scroll.setWidgetResizable(True)
        
        #debug
        self.tab1 = TabWidget()
        self.list.addWidget(self.tab1)
        
        self.list.addStretch()
        
        #adding to qwidget the layout
        self.w.setLayout(self.list)
        
        self.scroll.setWidget(self.w)
        self.addWidget(self.scroll)
        
class TabWidget(QFrame):
    def __init__(self):
        super().__init__()
        
        self.setMaximumHeight(100)
        
        self.main = QHBoxLayout()
        
        self.img = QFrame()
        self.img.setFixedSize(64,64)
        self.img.setStyleSheet("border: 1px solid lightgray; border-radius: 6px;")
        self.main.addWidget(self.img)
        
        self.vbox = QVBoxLayout()
        self.service_label = QLabel("GitHub")
        self.vbox.addWidget(self.service_label)
        self.username_label = QLabel("Username: grishatop1")
        self.vbox.addWidget(self.username_label)
        self.password_label = QLabel("Password: horsecookie123")
        self.vbox.addWidget(self.password_label)
        self.main.addLayout(self.vbox)
        
        self.options_layout = QVBoxLayout()
        self.edit_btn = QPushButton(text="Edit")
        self.options_layout.addWidget(self.edit_btn)
        self.remove_btn = QPushButton(text="Remove")
        self.remove_btn.setStyleSheet("color: lightred;")
        self.options_layout.addWidget(self.remove_btn)
        self.main.addLayout(self.options_layout)
        
        self.setLayout(self.main)
    

class SearchLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        
        self.addStretch()
        
        self.search = QLineEdit()
        self.search.setPlaceholderText("Search....")
        self.search.setMinimumWidth(500)
        self.search.setStyleSheet("padding: 5px;")
        self.addWidget(self.search)
        
        self.add_btn = QPushButton("+")
        self.add_btn.setStyleSheet("font-weight: bold;")
        self.add_btn.setMaximumWidth(50)
        self.addWidget(self.add_btn)
        
        self.addStretch()

class ToolbarLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.logo = QHBoxLayout()
        self.lock_label = QLabel()
        self.lock_pixmap = QPixmap("../assets/lock.png").scaledToWidth(32, Qt.SmoothTransformation)
        self.lock_label.setPixmap(self.lock_pixmap)
        self.logo.addWidget(self.lock_label)
        self.aes_text = QLabel(text="Fernet Encryption in use")
        self.logo.addWidget(self.aes_text)
        self.addLayout(self.logo)

        self.addStretch()

        self.logout_btn = QPushButton(text="Exit the safe")
        self.logout_btn.setStyleSheet("color: red;")
        self.addWidget(self.logout_btn)