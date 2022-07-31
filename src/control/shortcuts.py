from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut

class ShortcutsCtrl:
    def __init__(self, ctrl):
        self.ctrl = ctrl

        self.add_dialog1 = QShortcut(QKeySequence("Ctrl+t"), self.ctrl.ui)
        self.add_dialog1.activated.connect(self.add_dialog_open)
        self.add_dialog2 = QShortcut(QKeySequence("Ctrl+n"), self.ctrl.ui)
        self.add_dialog2.activated.connect(self.add_dialog_open)
        self.add_dialog3 = QShortcut(QKeySequence("f5"), self.ctrl.ui)
        self.add_dialog3.activated.connect(self.add_dialog_open)

        self.search_focus1 = QShortcut(QKeySequence("Ctrl+f"), self.ctrl.ui)
        self.search_focus1.activated.connect(self.focus_on_search)

    def add_dialog_open(self):
        if not self.ctrl.isMainActive(): return
        self.ctrl.main.openAddAccountDialog()

    def focus_on_search(self):
        if not self.ctrl.isMainActive(): return
        self.ctrl.ui.main_page.search.search.setFocus()