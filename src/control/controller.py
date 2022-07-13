from control.create import CreatePageCtrl

class Controller:
    def __init__(self, ui):
        self.ui = ui
        
        self.create = CreatePageCtrl(self)