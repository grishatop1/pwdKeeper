class BackCtrl:
    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.connectWidgets()
        
    def connectWidgets(self):
        self.ctrl.ui.login_page.bacc.btn.clicked.connect(self.go)
        self.ctrl.ui.create_page.bacc.btn.clicked.connect(self.go)
        
    def go(self):
        self.ctrl.ui.stacked.setCurrentIndex(0)
        self.ctrl.reset()