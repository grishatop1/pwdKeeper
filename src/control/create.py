from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtCore import QThread
from zxcvbn import zxcvbn

class CreatePageCtrl:
    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.connectWidgets()
        self.thread = None
        
        self.pwd = None
    
    def connectWidgets(self):
        self.ctrl.ui.create_page.pwd_entry.textChanged.connect(self.validate)
        self.ctrl.ui.create_page.pwd2_entry.textChanged.connect(self.validate)
        self.ctrl.ui.create_page.pwd2_entry.returnPressed.connect(self.proceed)
        self.ctrl.ui.create_page.enter_btn.clicked.connect(self.proceed)
        
    def validate(self):
        pwd1 = self.ctrl.ui.create_page.pwd_entry.text()
        pwd2 = self.ctrl.ui.create_page.pwd2_entry.text()
        if len(pwd1) < 6:
            self.setDisabled()
            self.uncheckPassword()
            return
        if pwd1 != pwd2:
            self.setDisabled()
            self.uncheckPassword()
            return
        
        self.checkPassword(pwd1)
        self.pwd = pwd1
        self.setEnabled()
        return True
    
    def checkPassword(self, pwd):
        result = zxcvbn(pwd)
        crack = result["crack_times_display"]["offline_slow_hashing_1e4_per_second"]

        self.ctrl.ui.create_page.crack_label.setText(f"Brute force time estimation: {crack}")
        
    def uncheckPassword(self):
        self.ctrl.ui.create_page.crack_label.setText("")
    
    def proceed(self):
        if not self.validate(): return #na svaki slucaj
        
        if self.thread:
            return
        
        self.ctrl.ui.create_page.enter_btn.setText("Creating...")
        self.ctrl.ui.create_page.bacc.btn.setDisabled(True)
        self.setDisabled()

        self.thread = QThread()
        self.worker = Worker(self.ctrl, self.pwd)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.done_signal.connect(self.thread.quit)
        self.worker.done_signal.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()
        
        self.thread.finished.connect(
            self.done
        )
        
    def done(self):
        self.thread = None
        self.ctrl.enterMain()
        
    def setEnabled(self):
        self.ctrl.ui.create_page.enter_btn.setDisabled(False)
        
    def setDisabled(self):
        self.ctrl.ui.create_page.enter_btn.setDisabled(True)
        
    def resetForm(self):
        self.ctrl.ui.create_page.enter_btn.setText("Enter!")
        self.setEnabled()
        self.ctrl.ui.create_page.pwd_entry.setText("")
        self.ctrl.ui.create_page.pwd2_entry.setText("")
        self.ctrl.ui.create_page.bacc.btn.setDisabled(False)
        self.uncheckPassword()
        
class Worker(QObject):
    done_signal = pyqtSignal()
    def __init__(self, ctrl, pwd):
        super().__init__()
        self.ctrl = ctrl
        self.pwd = pwd
        
    def run(self):
        self.ctrl.safe.create(self.pwd)
        self.done_signal.emit()