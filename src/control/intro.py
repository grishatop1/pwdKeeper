from PyQt5.QtWidgets import QFileDialog

class IntroCtrl:
    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.connectWidgets()
        
    def connectWidgets(self):
        self.ctrl.ui.intro_page.create_btn.clicked.connect(self.filePick)
        
    def filePick(self):
        dialog = QFileDialog()
        dialog.setDefaultSuffix(".pwdKeeper")
        path, _ = dialog.getSaveFileName(
            caption="Store database file",
            directory="myPasswords.pwdKeeper",
            filter="pwdKeeper file (*.pwdKeeper)"
        )
        
        if path:
            self.ctrl.safe.create(path)