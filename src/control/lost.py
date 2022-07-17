from PyQt5.QtWidgets import QFileDialog, QMessageBox
from os.path import expanduser
import os
import shutil

class LostCtrl:
    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.connectWidgets()
        self.path = None
        
    def setPath(self, path):
        self.path = path
        self.ctrl.ui.lost_page.path.setText(f"<b>{path}</b> is missing.")
        
    def connectWidgets(self):
        self.ctrl.ui.lost_page.idc_btn.clicked.connect(self.okLol)
        self.ctrl.ui.lost_page.locate_btn.clicked.connect(self.relocate)
        self.ctrl.ui.lost_page.load_btn.clicked.connect(self.fromBackup)
        
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
            
    def fromBackup(self):
        fname = os.path.basename(self.path)
        name, ext = os.path.splitext(fname)
        f = name + ".pwdBackup"
        b_file = os.path.join(self.ctrl.cache.PATH, f)
        if os.path.exists(b_file):
            try:
                future_path = os.path.join(self.ctrl.cache.PATH, "fromBackup")
                f_future_path = os.path.join(future_path, fname)
                os.makedirs(future_path, exist_ok=True)
                shutil.copyfile(b_file, f_future_path)
            except:
                dia = QMessageBox()
                dia.setText("Sorry, couldn't load the backup file")
                dia.setStandardButtons(QMessageBox.Ok)
                dia.exec()
                return
            self.ctrl.safe.setPath(f_future_path)
            self.ctrl.ui.stacked.setCurrentIndex(2)
            self.ctrl.ui.login_page.path_label.setText(
                f_future_path
            )
        else:
            dia = QMessageBox()
            dia.setText("Sorry, couldn't find the backup file...")
            dia.setStandardButtons(QMessageBox.Ok)
            dia.exec()
            