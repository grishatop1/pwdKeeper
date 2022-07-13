class IntroCtrl:
    def __init__(self, ctrl) -> None:
        self.ctrl = ctrl
        
    def connectWidgets(self):
        self.ctrl.ui.intro_page.create_btn.clicked.connect(self.createNewSafe)
        
    def createNewSafe(self):
        self.ctrl.safe.create()