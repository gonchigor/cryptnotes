import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

# password_provided = "password" # This is input in the form of a string

salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes


def get_key(password_provided):
    password = password_provided.encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once


def encrypt_message(message, password):
    key = get_key(password)
    message_provided = message.encode()
    f = Fernet(key)
    encrypted = f.encrypt(message_provided)
    return encrypted.decode()


def decrypt_message(message, password):
    key = get_key(password)
    message_provided = message.encode()
    f = Fernet(key)
    decrypted = f.decrypt(message_provided)
    return decrypted.decode()
