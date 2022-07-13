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
        
    def close(self, *args):
        if self.f:
            self.f.close()