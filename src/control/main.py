from gui.serviceDialog import ServiceDialog
from gui.main import TabWidget

class MainControl:
    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.connectWidgets()
        
        self.addDialog: ServiceDialog = None
        self.tabs = []
    
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
        
        self.ctrl.safe.addAccount(service, username, password)
        tab_ui = self.createTabWidget(service, username, password)
        self.appendTabWidget(tab_ui)
        self.addDialog.close()
        
    def loadEverything(self):
        data = self.ctrl.safe.data
        
        if not data:
            self.ctrl.ui.main_page.main.setEmptyLabel()
            return
        
        for tab in data:
            tab_ui = self.createTabWidget(
                tab["service"], tab["username"], tab["password"]
            )
            self.appendTabWidget(tab_ui)
            
       
            
    def createTabWidget(self, service, username, password):
        tab_ui = TabWidget()
        tab_ui.service_label.setText(service)
        tab_ui.username_label.setText(f"Username: <b>{username}</b>")
        tab_ui.password_label.setText(f"Password: <b>{password}</b>")
        return tab_ui
    
    def appendTabWidget(self, tab_ui: TabWidget):
        self.ctrl.ui.main_page.main.list.insertWidget(
            self.ctrl.ui.main_page.main.list.count()-1, tab_ui
        )
        self.ctrl.ui.main_page.main.removeEmptyLabel()
        self.tabs.append(tab_ui)
        
    def clearTabs(self):
        for tab in self.tabs:
            tab.deleteLater()