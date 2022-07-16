from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtCore import QThread

class LoginCtrl:
    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.connectWidgets()
        
        self.thread = None
        
    def connectWidgets(self):
        self.ctrl.ui.login_page.enter_btn.clicked.connect(self.proceed)
        self.ctrl.ui.login_page.pwd_entry.returnPressed.connect(self.proceed)
        self.ctrl.ui.login_page.pwd_entry.textChanged.connect(self.hideError)
        
    def proceed(self):
        
        if self.thread:
            return
        
        self.ctrl.ui.login_page.enter_btn.setText("Checking...")
        self.ctrl.ui.login_page.enter_btn.setDisabled(True)
        
        pwd = self.ctrl.ui.login_page.pwd_entry.text()
        
        self.thread = QThread()
        self.worker = Worker(self.ctrl, pwd)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.done_signal.connect(self.thread.quit)
        self.worker.done_signal.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()
        
        self.thread.finished.connect(
            lambda: self.done(self.worker.result)
        )
        
    def done(self, result):
        self.thread = None
        if result:
            self.ctrl.cache.writePath()
            self.ctrl.main.loadEverything()
            self.ctrl.ui.stacked.setCurrentIndex(3)
        else:
            self.showError("Wrong password!")
            self.ctrl.ui.login_page.enter_btn.setText("Enter!")
            self.ctrl.ui.login_page.enter_btn.setDisabled(False)
        
    def showError(self, text):
        self.ctrl.ui.login_page.error_label.setText(text)
        self.ctrl.ui.login_page.error_label.show()
        
    def hideError(self):
        self.ctrl.ui.login_page.error_label.hide()
        
    def resetForm(self):
        self.hideError()
        self.ctrl.ui.login_page.pwd_entry.setText("")
        self.ctrl.ui.login_page.enter_btn.setText("Enter!")
        self.ctrl.ui.login_page.enter_btn.setDisabled(False)
        
class Worker(QObject):
    done_signal = pyqtSignal()
    def __init__(self, ctrl, pwd):
        super().__init__()
        self.ctrl = ctrl
        self.pwd = pwd
        self.result = None
        
    def run(self):
        if self.ctrl.safe.f:
            self.result = self.ctrl.safe.load(self.pwd)
        self.done_signal.emit()