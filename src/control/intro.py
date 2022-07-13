from PyQt5.QtWidgets import QFileDialog
from os.path import expanduser

class IntroCtrl:
    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.connectWidgets()
        
    def connectWidgets(self):
        self.ctrl.ui.intro_page.create_btn.clicked.connect(self.createSafePick)
        
    def createSafePick(self):
        dialog = QFileDialog()
        dialog.setDefaultSuffix(".pwdKeeper")
        path, _ = dialog.getSaveFileName(
            caption="Store database file",
            directory=f"{expanduser('~')}/myPasswords.pwdKeeper",
            filter="pwdKeeper file (*.pwdKeeper)"
        )
        
        if path:
            self.ctrl.safe.setPath(path)
            self.ctrl.ui.stacked.setCurrentIndex(1)