import os
import base64
import pickle
from io import BytesIO
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
        self.prepend = BytesIO()
        
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
        kdf_hash = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=500000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        _hash = kdf_hash.derive(key)

        self.fnet = Fernet(key)
        self.prepend.write(salt)
        self.prepend.write(_hash)
        self.save()
        #salt16 + hash32 = first 48 bytes for auth
        
    def load(self, pwd):
        self.f = open(self.path, "wb+")
        password = pwd.encode("utf-8")
        
    def close(self, *args):
        if self.f:
            self.f.close()
            
    def save(self):
        data = pickle.dumps(self.data)
        ciphertext = self.fnet.encrypt(data)
        prepend = self.prepend.read()
        self.f.write(prepend)
        self.f.write(ciphertext)
        self.prepend.seek(0)
            
    def addAccount(self, service, username, password):
        acc = {
            "service": service,
            "username": username,
            "password": password
        }
        self.data.append(acc)
        self.save()