import os
import pickle

class CacheManager:
    PATH = os.path.join(
        os.path.expanduser("~"),
        ".pwdKeeper"
    )
    FPATH = os.path.join(
        PATH,
        "cache"
    )
    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.f = None
        self.load()
        
    def writePath(self):
        data = {
            "lastPath": self.ctrl.safe.path
        }
        try:
            with open(self.FPATH, "wb") as f:
                pickle.dump(data, f)
        except:
            return
        
    def removePath(self):
        try:
            with open(self.FPATH, "wb") as f:
                pickle.dump({"lastPath": None}, f)
        except:
            return
    
    def load(self):
        if not os.path.exists(self.PATH):
            os.makedirs(self.PATH)
        if not os.path.exists(self.FPATH):
            return
        
        try:
            with open(self.FPATH, "rb") as f:
                data = pickle.load(f)
        except:
            return
        
        if not data["lastPath"]:
            return
        
        if not os.path.exists(data["lastPath"]):
            return
        
        self.ctrl.ui.login_page.path_label.setText(
            data["lastPath"]
        )
        self.ctrl.safe.setPath(data["lastPath"])
        self.ctrl.ui.stacked.setCurrentIndex(2)