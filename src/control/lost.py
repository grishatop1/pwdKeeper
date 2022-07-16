from PyQt5.QtWidgets import QFileDialog
from os.path import expanduser

class LostCtrl:
    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.connectWidgets()
        
    def connectWidgets(self):
        self.ctrl.ui.lost_page.idc_btn.clicked.connect(self.okLol)
        self.ctrl.ui.lost_page.locate_btn.clicked.connect(self.relocate)
        
    def okLol(self):
        self.ctrl.cache.removePath()
        self.ctrl.ui.stacked.setCurrentIndex(0)
        
    def relocate(self):
        dialog = QFileDialog()
        path, _ = dialog.getOpenFileName(
            caption="Select pwdKeeper file",
            filter="pwdKeeper file (*.pwdKeeper)",
            directory=f"{expanduser('~')}/"
        )
        if path:
            self.ctrl.cache.removePath()
            self.ctrl.safe.setPath(path)
            self.ctrl.ui.stacked.setCurrentIndex(2)
            self.ctrl.ui.login_page.path_label.setText(
                path
            )