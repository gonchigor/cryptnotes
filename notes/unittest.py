import unittest
from .crypto import encrypt_message, decrypt_message
from cryptography.fernet import InvalidToken, InvalidSignature


class TestCryptoModule(unittest.TestCase):
    def setUp(self):
        self.text = encrypt_message('text', '123')

    def test_encrypt(self):
        self.assertNotEqual(encrypt_message('text', '123456'), 'text')

    def test_decrypt(self):
        self.assertEqual(decrypt_message(self.text, '123'), 'text')

    def test_wrong_password(self):
        self.assertRaises(InvalidToken, decrypt_message, self.text, '456')


if __name__ == '__main__':
    unittest.main()
