from PyQt5.QtWidgets import QFileDialog
from os.path import expanduser

class IntroCtrl:
    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.connectWidgets()
        
    def connectWidgets(self):
        self.ctrl.ui.intro_page.create_btn.clicked.connect(self.createSafePick)
        self.ctrl.ui.intro_page.load_btn.clicked.connect(self.loadSafePick)
        
    def createSafePick(self):
        dialog = QFileDialog()
        dialog.setDefaultSuffix(".pwdKeeper")
        path, _ = dialog.getSaveFileName(
            caption="Store pwdKeeper file",
            directory=f"{expanduser('~')}/myPasswords.pwdKeeper",
            filter="pwdKeeper file (*.pwdKeeper)"
        )
        
        if path:
            self.ctrl.safe.setPath(path)
            self.ctrl.ui.stacked.setCurrentIndex(1)
            self.ctrl.ui.create_page.path_label.setText(
                path
            )
            
    def loadSafePick(self):
        dialog = QFileDialog()
        path, _ = dialog.getOpenFileName(
            caption="Select pwdKeeper file",
            filter="pwdKeeper file (*.pwdKeeper)",
            directory=f"{expanduser('~')}/"
        )
        if path:
            self.ctrl.safe.setPath(path)
            self.ctrl.ui.stacked.setCurrentIndex(2)
            self.ctrl.ui.login_page.path_label.setText(
                path
            )