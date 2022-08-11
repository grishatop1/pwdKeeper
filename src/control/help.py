from gui.help import HelpWindow

class HelpCtrl:
    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.connectWidgets()
        self.path = None

        self.dia = None

    def connectWidgets(self):
        self.ctrl.ui.main_page.toolbar.help_btn.clicked.connect(self.openHelpWindow)
        self.ctrl.ui.intro_page.help_btn.clicked.connect(self.openHelpWindow)

    def openHelpWindow(self):
        self.dia = HelpWindow()
        self.dia.show()
        