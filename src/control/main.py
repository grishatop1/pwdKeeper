from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

from gui.serviceDialog import EditTab, ServiceDialog
from gui.main import TabWidget

class MainControl:
    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.connectWidgets()
        
        self.addDialog: ServiceDialog = None
        self.tabs = []
        self.selectedTab = None
        self.dialog = None
    
    def connectWidgets(self):
        self.ctrl.ui.main_page.search.search.textChanged.connect(self.search)
        self.ctrl.ui.main_page.search.add_btn.clicked.connect(self.openAddAccountDialog)
        self.ctrl.ui.main_page.toolbar.logout_btn.clicked.connect(self.backToTheLobby)
        
    def search(self):
        srch = self.ctrl.ui.main_page.search.search.text()
        srch = srch.lower()
        for tab in self.tabs:
            service = tab.service.lower()
            username = tab.username.lower()
            password = tab.password.lower()
            if not srch in service and not srch in username and not srch in password:
                tab.ui.hide()
            else:
                tab.ui.show()
        
    def backToTheLobby(self):
        self.ctrl.cache.removePath()
        self.ctrl.ui.stacked.setCurrentIndex(0)
        self.ctrl.reset()
    
    def openAddAccountDialog(self):
        usernames = []
        for _id, data in self.ctrl.safe.data.items():
            usernames.append(data["username"])
        self.dialog = ServiceDialog(list(set(usernames)))
        self.dialog.add_btn.clicked.connect(self.addAccount)
        self.dialog.exec()
        
    def addAccount(self):
        service = self.dialog.combox.currentText()
        username = self.dialog.username_combox.currentText()
        password = self.dialog.password_entry.text()
        if service == "" or username == "" or password == "":
            return
        _id = self.ctrl.safe.addAccount(service, username, password)
        tab = Tab(self, _id, service, username, password)
        self.tabs.append(tab) 
        self.dialog.close()
        self.dialog = None
        
    def loadEverything(self):
        data = self.ctrl.safe.data
        
        for _id, _tab in data.items():
            tab = Tab(self, _id, _tab["service"], _tab["username"], _tab["password"])
            self.tabs.append(tab)
            
        if not data:
            self.ctrl.ui.main_page.main.empty_label.show()
            
        self.ctrl.ui.main_page.toolbar.txt.setText(
            f"<font color='gray'>{self.ctrl.safe.fname}</font> - autosave is <font color='lightgreen'>on</font>"
        )
    
    def openRemoveAccountDialog(self, tab):
        self.selectedTab = tab
        dialog = QMessageBox()
        dialog.setText("Do u really want to remove this account?")
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dialog.buttonClicked.connect(self.removeTab)
        dialog.exec()
        
    def removeTab(self, i):
        if i.text() == "&Yes":
            self.ctrl.safe.removeAccount(self.selectedTab._id)
            self.selectedTab.remove()
            self.tabs.remove(self.selectedTab)
            if not self.ctrl.safe.data:
                self.ctrl.ui.main_page.main.empty_label.show()
        
    def clearTabs(self):
        for tab in self.tabs:
            tab.remove()
        self.tabs = []
        
        
class Tab:
    def __init__(self, main, _id, service, username, password):
        self.main = main
        self._id = _id
        self.service = service
        self.username = username
        self.password = password
        self.ui = TabWidget()
        self.dialog = None
        self.setUI()
        self.setUIBindings()
        self.addToUI()
        
        self.copyUsernameTimer = None
        self.copyPasswordTimer = None
        
    def setUI(self):
        self.ui.service_label.setText(self.service)
        self.setUIUsername()
        self.setUIPassword()

    def setUIUsername(self):
        self.ui.username_label.setText(f"Username: <b>{self.username}</b>")
        self.copyUsernameTimer = None
        self.ui.username_label.setStyleSheet("")

    def setUIPassword(self):
        self.ui.password_label.setText(f"Password: <b>***</b>")
        self.copyPasswordTimer = None
        self.ui.password_label.setStyleSheet("")
        
    def setUIBindings(self):
        self.ui.edit_btn.clicked.connect(self.openEditAccountDialog)
        self.ui.remove_btn.clicked.connect(lambda: self.main.openRemoveAccountDialog(self))
        self.ui.password_label.enterEvent = self.showPass
        self.ui.password_label.leaveEvent = self.hidePass
        self.ui.username_label.mousePressEvent = self.copyUsername
        self.ui.password_label.mousePressEvent = self.copyPassword
        
    def addToUI(self):
        self.main.ctrl.ui.main_page.main.list.insertWidget(
            self.main.ctrl.ui.main_page.main.list.count()-1,self.ui
        )
        self.main.ctrl.ui.main_page.main.empty_label.hide()
        
    def remove(self):
        self.ui.deleteLater()
        
    def openEditAccountDialog(self):
        self.dialog = EditTab(self.service, self.username, self.password)
        self.dialog.change_btn.clicked.connect(self.edit)
        self.dialog.exec()
        
    def edit(self):
        self.service = self.dialog.combox.currentText()
        self.username = self.dialog.username_entry.text()
        self.password = self.dialog.password_entry.text()
        self.main.ctrl.safe.editAccount(self._id, self.service, self.username, self.password)
        self.setUI()
        self.dialog.close()
        
    def showPass(self, *args):
        if self.copyPasswordTimer: return
        self.ui.password_label.setText(f"Password: <b>{self.password}</b>")
        
    def hidePass(self, *args):
        if self.copyPasswordTimer: return
        self.ui.password_label.setText(f"Password: <b>***</b>")
        
    def copyUsername(self, *args):
        if self.copyUsernameTimer: return
        self.ui.username_label.setText("<b>Copied to clipboard!</b>")
        self.ui.username_label.setStyleSheet("color: lightgreen;")
        self.copyUsernameTimer = QTimer()
        self.copyUsernameTimer.setSingleShot(True)
        self.copyUsernameTimer.start(500)
        self.copyUsernameTimer.timeout.connect(self.setUIUsername)
        QApplication.clipboard().setText(self.username)
        
    def copyPassword(self, *args):
        if self.copyPasswordTimer: return
        self.ui.password_label.setText("<b>Copied to clipboard!</b>")
        self.ui.password_label.setStyleSheet("color: lightgreen;")
        self.copyPasswordTimer = QTimer()
        self.copyPasswordTimer.setSingleShot(True)
        self.copyPasswordTimer.start(500)
        self.copyPasswordTimer.timeout.connect(self.setUIPassword)
        QApplication.clipboard().setText(self.password)