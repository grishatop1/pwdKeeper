from .bacc import BackCtrl
from .cache import CacheManager
from .create import CreatePageCtrl
from .intro import IntroCtrl
from .login import LoginCtrl
from .lost import LostCtrl
from .main import MainControl
from .safe import SafeControl
from .shortcuts import ShortcutsCtrl
from .help import HelpCtrl

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