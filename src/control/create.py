class CreatePageCtrl:
    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.connectWidgets()
    
    def connectWidgets(self):
        self.ctrl.ui.create_page.pwd_entry.textChanged.connect(self.validate)
        self.ctrl.ui.create_page.pwd2_entry.textChanged.connect(self.validate)
        self.ctrl.ui.create_page.pwd2_entry.returnPressed.connect(self.proceed)
        self.ctrl.ui.create_page.enter_btn.clicked.connect(self.proceed)
        
    def validate(self):
        pwd1 = self.ctrl.ui.create_page.pwd_entry.text()
        pwd2 = self.ctrl.ui.create_page.pwd2_entry.text()
        if len(pwd1) < 6:
            self.setDisabled()
            return
        if pwd1 != pwd2:
            self.setDisabled()
            return
        
        self.setEnabled()
        return True
    
    def proceed(self):
        if not self.validate(): return #na svaki slucaj
        
        
    def setEnabled(self):
        self.ctrl.ui.create_page.enter_btn.setDisabled(False)
        
    def setDisabled(self):
        self.ctrl.ui.create_page.enter_btn.setDisabled(True)