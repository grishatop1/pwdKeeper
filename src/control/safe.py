import os
import base64
import json
import uuid
import shutil
import datetime
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class SafeControl:
    def __init__(self, ctrl):
        self.ctrl = ctrl
        
        self.path: str = None
        self.fname = None
        self.f = None
        self.fnet: Fernet = None
        self.data = {}
        self.prepend = None
        
    def setPath(self, path):
        self.path = path
        self.fname = os.path.basename(self.path)
        
    def create(self, pwd):
        self.f = open(self.path, "wb+")
        
        password = pwd.encode("utf-8")
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=500000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        digest = hashes.Hash(hashes.SHA256(), default_backend())
        digest.update(key)
        _hash = digest.finalize()
        
        self.fnet = Fernet(key)
        self.prepend = salt + _hash
        self.save()
        #salt16 + hash32 = first 48 bytes for auth
        
    def load(self, pwd):
        self.f = open(self.path, "rb+")
        password = pwd.encode("utf-8")
        salt = self.f.read(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=500000,
            backend=default_backend()
        )
        usr_key = base64.urlsafe_b64encode(kdf.derive(password))
        digest = hashes.Hash(hashes.SHA256(), default_backend())
        digest.update(usr_key)
        user_hash = digest.finalize()
        _hash = self.f.read(32)
        if user_hash != _hash:
            return
        
        self.fnet = Fernet(usr_key)
        self.prepend = salt + _hash
        
        rawdata = self.f.read()
        data = self.fnet.decrypt(rawdata)
        self.data = json.loads(data.decode("utf-8"))
        return True
        
    def close(self, *args):
        try:
            self.makeBackup()
        except:
            pass
        if self.f:
            self.f.close()
            
    def makeBackup(self):
        f, _ = os.path.splitext(self.path)
        fname = os.path.basename(f)
        newPath = os.path.join(
                self.ctrl.cache.PATH, 
                f"{fname}.pwdBackup"
            )
        try:
            os.remove(newPath)
        except:
            pass
        shutil.copyfile(
            self.path,
            newPath
        )
            
    def save(self):
        data = json.dumps(self.data)
        ciphertext = self.fnet.encrypt(data.encode("utf-8"))
        self.f.seek(0)
        self.f.write(self.prepend)
        self.f.write(ciphertext)
        self.f.truncate()
            
    def addAccount(self, service, username, password):
        _id = str(uuid.uuid4())
        acc = {
            "service": service,
            "username": username,
            "password": password
        }
        self.data[_id] = acc
        self.save()
        return _id
    
    def editAccount(self, _id, service, username, password):
        acc = {
            "service": service,
            "username": username,
            "password": password
        }
        self.data[_id] = acc
        self.save()
        
    def removeAccount(self, _id):
        del self.data[_id]
        self.save()
        
    def reset(self):
        self.close()
        self.path: str = None
        self.f = None
        self.fnet: Fernet = None
        self.data = {}
        self.prepend = None