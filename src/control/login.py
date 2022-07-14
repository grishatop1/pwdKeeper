class LoginCtrl:
    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.connectWidgets()
        
    def connectWidgets(self):
        self.ctrl.ui.login_page.enter_btn.clicked.connect(self.proceed)
        self.ctrl.ui.login_page.pwd_entry.returnPressed.connect(self.proceed)
        
    def proceed(self):
        pwd = self.ctrl.ui.login_page.pwd_entry.text()
        result = self.ctrl.safe.load(pwd)