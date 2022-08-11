from control.bacc import BackCtrl
from control.cache import CacheManager
from control.create import CreatePageCtrl
from control.intro import IntroCtrl
from control.login import LoginCtrl
from control.lost import LostCtrl
from control.main import MainControl
from control.safe import SafeControl
from control.shortcuts import ShortcutsCtrl
from control.help import HelpCtrl

class Controller:
    def __init__(self, ui):
        self.ui = ui

        self.safe = SafeControl(self)
        
        self.intro = IntroCtrl(self)
        self.create = CreatePageCtrl(self)
        self.login = LoginCtrl(self)
        self.main = MainControl(self)
        self.bacc = BackCtrl(self)
        self.help = HelpCtrl(self)
        
        self.lost = LostCtrl(self)
        self.cache = CacheManager(self)
        self.shortcuts = ShortcutsCtrl(self)
        
        self.ui.closeEvent = self.safe.close
        
    def reset(self):
        self.login.resetForm()
        self.create.resetForm()
        self.safe.reset()
        self.main.clearTabs()
        
    def enterMain(self):
        self.cache.writePath()
        self.main.loadEverything()
        self.ui.stacked.setCurrentIndex(3)

    def isMainActive(self):
        if self.ui.stacked.currentIndex() == 3:
            return True