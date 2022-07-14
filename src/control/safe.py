import os
import base64
import pickle
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class SafeControl:
    def __init__(self, ctrl):
        self.ctrl = ctrl
        
        self.path: str = None
        self.f = None
        self.fnet: Fernet = None
        self.data = []
        self.prepend = b""
        
    def setPath(self, path):
        self.path = path
        
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
        self.data = pickle.loads(data)
        return True
        
        
    def close(self, *args):
        if self.f:
            self.f.close()
            
    def save(self):
        data = pickle.dumps(self.data)
        ciphertext = self.fnet.encrypt(data)
        self.f.write(self.prepend + ciphertext)
            
    def addAccount(self, service, username, password):
        acc = {
            "service": service,
            "username": username,
            "password": password
        }
        self.data.append(acc)
        self.save()