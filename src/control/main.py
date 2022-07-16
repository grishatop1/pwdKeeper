from PyQt5.QtWidgets import QMessageBox

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
        self.ctrl.ui.main_page.search.add_btn.clicked.connect(self.openAddAccountDialog)
        self.ctrl.ui.main_page.toolbar.logout_btn.clicked.connect(self.backToTheLobby)
        
    def backToTheLobby(self):
        self.ctrl.ui.stacked.setCurrentIndex(0)
        self.ctrl.reset()
    
    def openAddAccountDialog(self):
        self.dialog = ServiceDialog()
        self.dialog.add_btn.clicked.connect(self.addAccount)
        self.dialog.exec()
        
    def addAccount(self):
        service = self.dialog.combox.currentText()
        username = self.dialog.username_entry.text()
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
        
    def setUI(self):
        self.ui.service_label.setText(self.service)
        self.ui.username_label.setText(f"Username: <b>{self.username}</b>")
        self.ui.password_label.setText(f"Password: <b>{self.password}</b>")
        
    def setUIBindings(self):
        self.ui.edit_btn.clicked.connect(self.openEditAccountDialog)
        self.ui.remove_btn.clicked.connect(lambda: self.main.openRemoveAccountDialog(self))
        
    def addToUI(self):
        self.main.ctrl.ui.main_page.main.list.insertWidget(
            self.main.ctrl.ui.main_page.main.list.count()-1,self.ui
        )
        
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