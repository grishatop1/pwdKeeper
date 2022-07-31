from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPixmap, QColor

from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtWidgets import QStackedLayout

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
        self.list_w = QWidget()
        self.list = QVBoxLayout()
        self.stacked = QStackedLayout()
        
        self.stacked.setStackingMode(QStackedLayout.StackAll)
        self.scroll.setWidgetResizable(True)
        self.list.setContentsMargins(15,15,15,15)
        self.list.setSpacing(30)
        
        self.list.addStretch()
        
        self.list_w.setLayout(self.list)
        
        self.stacked.addWidget(self.list_w)
        
        self.empty_label = QLabel("Uh, such an empty place...")
        self.empty_label.setAlignment(Qt.AlignCenter)
        self.empty_label.setStyleSheet("color: #525252; font-size: 20px; font-weight: bold; background-color: transparent;")
        self.empty_label.hide()
        self.stacked.addWidget(self.empty_label)
        
        #adding to qwidget the layout
        self.w.setLayout(self.stacked)
        
        self.scroll.setWidget(self.w)
        self.addWidget(self.scroll)
        
class TabWidget(QFrame):
    def __init__(self):
        super().__init__()
        
        self.setMaximumHeight(100)
        self.setStyleSheet("border-radius: 10px;")
        
        self.shadow = QGraphicsDropShadowEffect(self,
            blurRadius=15.0,
            offset=QPointF(0,0),
            color=QColor(0,0,0, 60)
        )
        
        self.main = QHBoxLayout()

        self.service_layout = QHBoxLayout()
        self.main.addLayout(self.service_layout)

        self.service_logo = QLabel()
        self.service_layout.addWidget(self.service_logo)

        self.service_layout.addSpacing(25)

        self.service_label = QLabel()
        self.service_label.setStyleSheet("font-weight: bold; font-size: 17px;")
        self.service_label.setMinimumWidth(100)
        #self.service_label.setAlignment(Qt.AlignCenter)
        self.service_layout.addWidget(self.service_label)

        self.service_layout.addStretch()

        self.main.addSpacing(80)
        
        self.vbox = QVBoxLayout()
        self.main.addLayout(self.vbox, 2)
        self.vbox.addStretch()
        self.username_label = QLabel("Username: grishatop1")
        self.vbox.addWidget(self.username_label)
        self.password_label = QLabel("Password: horsecookie123")
        self.vbox.addWidget(self.password_label)
        self.vbox.addStretch()
        
        
        self.options_layout = QVBoxLayout()
        self.edit_btn = QPushButton(text="Edit")
        self.options_layout.addWidget(self.edit_btn)
        self.remove_btn = QPushButton(text="Remove")
        self.remove_btn.setStyleSheet("color: red;")
        self.options_layout.addWidget(self.remove_btn)
        self.main.addLayout(self.options_layout)
        
        self.setLayout(self.main)
        self.setGraphicsEffect(self.shadow)

class SearchLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        
        self.addStretch()
        
        self.search = QLineEdit()
        self.search.setPlaceholderText("Search....")
        self.search.setMinimumWidth(500)
        self.search.setStyleSheet(r"QLineEdit:focus {border: 1px solid #03fccf;} QLineEdit {padding:7px;}")
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
        self.lock_pixmap = QPixmap("../assets/safe-icon.png").scaledToWidth(36, Qt.SmoothTransformation)
        self.lock_label.setPixmap(self.lock_pixmap)
        self.logo.addWidget(self.lock_label)
        self.txt = QLabel()
        self.logo.addWidget(self.txt)
        self.addLayout(self.logo)

        self.addStretch()

        self.logout_btn = QPushButton(text="Change the safe")
        self.addWidget(self.logout_btn)