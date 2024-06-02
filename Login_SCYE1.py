from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
import os
#! pip install cryptography if its showing error (Make sure you're in the virtual env day_zero_one)

class DictionaryEncryptor:
    def __init__(self, passphrase, salt=None):
        self.passphrase = passphrase.encode()
        self.salt = salt if salt else os.urandom(16)
        self.key = self.derive_key(self.passphrase, self.salt)
        self.cipher_suite = Fernet(self.key)

    def derive_key(self, passphrase, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return base64.urlsafe_b64encode(kdf.derive(passphrase))

    def encrypt(self, data):
        encrypted_data = {}
        for k, v in data.items():
            if isinstance(v, dict):
                encrypted_data[k] = self.encrypt(v)
            else:
                encrypted_data[k] = self.cipher_suite.encrypt(v.encode()).decode()
        return encrypted_data

    def decrypt(self, data):
        decrypted_data = {}
        for k, v in data.items():
            if isinstance(v, dict):
                decrypted_data[k] = self.decrypt(v)
            else:
                decrypted_data[k] = self.cipher_suite.decrypt(v.encode()).decode()
        return decrypted_data

    def get_salt(self):
        return self.salt