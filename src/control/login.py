class LoginCtrl:
    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.connectWidgets()
        
    def connectWidgets(self):
        self.ctrl.ui.login_page.enter_btn.clicked.connect(self.proceed)
        self.ctrl.ui.login_page.pwd_entry.returnPressed.connect(self.proceed)
        self.ctrl.ui.login_page.pwd_entry.textChanged.connect(self.hideError)
        
    def proceed(self):
        pwd = self.ctrl.ui.login_page.pwd_entry.text()
        result = self.ctrl.safe.load(pwd)
        if not result:
            self.showError("Wrong password!")
            return
        
        self.ctrl.main.loadEverything()
        self.ctrl.ui.stacked.setCurrentIndex(3)
        
    def showError(self, text):
        self.ctrl.ui.login_page.error_label.setText(text)
        self.ctrl.ui.login_page.error_label.show()
        
    def hideError(self):
        self.ctrl.ui.login_page.error_label.hide()
        
    def resetForm(self):
        self.hideError()
        self.ctrl.ui.login_page.pwd_entry.setText("")