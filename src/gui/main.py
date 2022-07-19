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
        self.list.setContentsMargins(15,15,15,15)
        self.list.setSpacing(10)
        
        self.list.addStretch()
        
        #adding to qwidget the layout
        self.w.setLayout(self.list)
        
        self.scroll.setWidget(self.w)
        self.addWidget(self.scroll)
        
    def setEmptyLabel(self):
        self.label = QLabel("Such an empty place here :3")
        self.label.setStyleSheet("color: #525252; font-size: 20px; font-weight: bold;")
        self.label.setAlignment(Qt.AlignCenter)
        self.list.insertWidget(0, self.label)
        
        
    def removeEmptyLabel(self):
        self.label.deleteLater()
        self.label_hidden = True
        self.list.addStretch()
        
class TabWidget(QFrame):
    def __init__(self):
        super().__init__()
        
        self.setMaximumHeight(100)
        
        self.main = QHBoxLayout()

        self.service_label = QLabel()
        self.service_label.setStyleSheet("font-weight: bold; font-size: 17px;")
        self.service_label.setMinimumWidth(200)
        self.service_label.setAlignment(Qt.AlignCenter)
        self.main.addWidget(self.service_label)
        
        self.main.addSpacing(25)
        
        self.vbox = QVBoxLayout()
        self.vbox.addStretch()
        self.username_label = QLabel("Username: grishatop1")
        self.vbox.addWidget(self.username_label)
        self.password_label = QLabel("Password: horsecookie123")
        self.vbox.addWidget(self.password_label)
        self.vbox.addStretch()
        self.main.addLayout(self.vbox, 2)
        
        self.options_layout = QVBoxLayout()
        self.edit_btn = QPushButton(text="Edit")
        self.options_layout.addWidget(self.edit_btn)
        self.remove_btn = QPushButton(text="Remove")
        self.remove_btn.setStyleSheet("color: red;")
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
        self.search.setStyleSheet("padding: 7px;")
        self.addWidget(self.search)
        
        self.add_btn = QPushButton("+")
        self.add_btn.setStyleSheet("font-weight: bold; color: lightgreen;")
        self.add_btn.setFixedWidth(50)
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
        self.aes_text = QLabel(text="AES 128bit encryption")
        self.logo.addWidget(self.aes_text)
        self.addLayout(self.logo)

        self.addStretch()

        self.logout_btn = QPushButton(text="Change the safe")
        self.addWidget(self.logout_btn)