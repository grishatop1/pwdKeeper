from gui.serviceDialog import ServiceDialog

class MainControl:
    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.connectWidgets()
        
        self.addDialog: ServiceDialog = None
    
    def connectWidgets(self):
        self.ctrl.ui.main_page.search.add_btn.clicked.connect(self.openAddAccountDialog)
    
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
        self.addDialog.close()