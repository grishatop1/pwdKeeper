from control.create import CreatePageCtrl
from control.intro import IntroCtrl
from control.main import MainControl
from control.safe import SafeControl

class Controller:
    def __init__(self, ui):
        self.ui = ui

        self.safe = SafeControl(self)
        
        self.intro = IntroCtrl(self)
        self.create = CreatePageCtrl(self)
        self.main = MainControl(self)
        
        self.ui.closeEvent = self.safe.close