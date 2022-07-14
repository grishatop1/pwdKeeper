import os
import base64
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
        self.f.write(salt)
        self.f.write(_hash)
        
        #salt16 + hash32 = first 48 bytes for auth
        
    def close(self, *args):
        if self.f:
            self.f.close()