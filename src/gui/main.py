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
        
        #debug
        self.tab1 = TabWidget()
        
        self.scroll.setWidgetResizable(True)
        
        self.addWidget(self.scroll)
        
class TabWidget(QFrame):
    def __init__(self):
        super().__init__()
        
        self.main = QHBoxLayout()
        
        self.img = QFrame()
        self.img.resize(64,64)
        self.img.setStyleSheet("border: 1px solid lightgray; border-radius: 6px;")
        
        self.main.addWidget(self.img)
        
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