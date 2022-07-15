from PyQt5.QtWidgets import QMessageBox

from gui.serviceDialog import EditTab, ServiceDialog
from gui.main import TabWidget

class MainControl:
    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.connectWidgets()
        
        self.addDialog: ServiceDialog = None
        self.tabs = []
        self.tabToRemove = None
        self.tabToEdit = None
    
    def connectWidgets(self):
        self.ctrl.ui.main_page.search.add_btn.clicked.connect(self.openAddAccountDialog)
        self.ctrl.ui.main_page.toolbar.logout_btn.clicked.connect(self.backToTheLobby)
        
    def backToTheLobby(self):
        self.ctrl.ui.stacked.setCurrentIndex(0)
        self.ctrl.reset()
    
    def openAddAccountDialog(self):
        self.addDialog = ServiceDialog()
        self.addDialog.add_btn.clicked.connect(self.addAccount)
        self.addDialog.exec()
        
    def addAccount(self):
        service = self.addDialog.combox.currentText()
        username = self.addDialog.username_entry.text()
        password = self.addDialog.password_entry.text()
        if service == "" or username == "" or password == "":
            return
        
        _id = self.ctrl.safe.addAccount(service, username, password)
        tab_ui = self.createTabWidget(service, username, password)
        tab_ui.setId(_id)
        self.appendTabWidget(tab_ui)
        self.addDialog.close()
        
    def openEditAccountDialog(self, tab_ui):
        tab = self.ctrl.safe.data[tab_ui._id]
        self.tabToEdit = tab_ui
        self.editDialog = EditTab(
            tab["service"], tab["username"], tab["password"]
        )
        self.editDialog.change_btn.clicked.connect(self.editTab)
        self.editDialog.exec()
        
    def editTab(self):
        service = self.editDialog.combox.currentText()
        username = self.editDialog.username_entry.text()
        password = self.editDialog.password_entry.text()
        self.ctrl.safe.editAccount(self.tabToEdit._id, service, username, password)
        self.tabToEdit.service_label.setText(service)
        self.tabToEdit.username_label.setText(f"Username: <b>{username}</b>")
        self.tabToEdit.password_label.setText(f"Password: <b>{password}</b>")
        self.tabToEdit = None
        self.editDialog.close()
        
    def loadEverything(self):
        data = self.ctrl.safe.data
        
        for _id, tab in data.items():
            tab_ui = self.createTabWidget(
                tab["service"], tab["username"], tab["password"]
            )
            tab_ui.setId(_id)
            self.appendTabWidget(tab_ui)
       
            
    def createTabWidget(self, service, username, password):
        tab_ui = TabWidget()
        tab_ui.service_label.setText(service)
        tab_ui.username_label.setText(f"Username: <b>{username}</b>")
        tab_ui.password_label.setText(f"Password: <b>{password}</b>")
        tab_ui.remove_btn.clicked.connect(lambda: self.askToRemoveTab(tab_ui))
        tab_ui.edit_btn.clicked.connect(lambda: self.openEditAccountDialog(tab_ui))
        return tab_ui
    
    def askToRemoveTab(self, tab_ui):
        self.tabToRemove = tab_ui
        dialog = QMessageBox()
        dialog.setText("Do u really want to remove this account?")
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dialog.buttonClicked.connect(self.tabRemoovation)
        dialog.exec()
        
    def tabRemoovation(self, i):
        if i.text() == "&Yes":
            self.removeTab()
    
    def removeTab(self):
        self.tabs.remove(self.tabToRemove)
        self.tabToRemove.deleteLater()
        self.ctrl.safe.removeAccount(self.tabToRemove._id)
        self.tabToRemove = None
        
    def appendTabWidget(self, tab_ui: TabWidget):
        self.ctrl.ui.main_page.main.list.insertWidget(
            self.ctrl.ui.main_page.main.list.count()-1,tab_ui
        )
        self.tabs.append(tab_ui)
        
    def clearTabs(self):
        for tab in self.tabs:
            tab.deleteLater()
        self.tabs = []
        
        
class Tab:
    def __init__(self, ctrl, _id, service, username, password):
        self.ctrl = ctrl
        self._id = _id
        self.service = service
        self.username = username
        self.password = password
        self.ui = TabWidget()