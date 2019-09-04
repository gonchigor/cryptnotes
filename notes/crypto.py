import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from passlib.hash import pbkdf2_sha256


salt = b'salt_'


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


def password_hasher(password):
    return pbkdf2_sha256.hash(password)


def password_verify(password, hash_):
    return pbkdf2_sha256.verify(password, hash_)
