import os
import logging

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

logger = logging.getLogger()
logger.setLevel('INFO')

def generate_symmetric_key(length: int) -> bytes:
    key = os.urandom(length)
    logging.info(f'Symmetric key successfully generated (key length: {length} bytes)')
    return key

def symmetric_encrypt(key: bytes, text: bytes) -> bytes:
    padder = padding.ANSIX923(64).padder()
    padded_text = padder.update(text) + padder.finalize()
    iv = os.urandom(8)
    cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    cipher_text = encryptor.update(padded_text) + encryptor.finalize()
    logging.info('Symmetric encryption was successful')
    return iv + cipher_text

def symmetric_decrypt(key: bytes, cipher_text: bytes) -> bytes:
    cipher_text, iv = cipher_text[8:], cipher_text[:8]
    cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    text = decryptor.update(cipher_text) + decryptor.finalize()
    unpadder = padding.ANSIX923(64).unpadder()
    unpadded_text = unpadder.update(text) + unpadder.finalize()
    logging.info('Symmetric decryption was successful')
    return unpadded_text