import os
import logging

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

logger = logging.getLogger()
logger.setLevel('INFO')

def generate_symmetric_key(length: int) -> bytes:
    key = os.urandom(length)
    logging.info(f' Symmetric key successfully generated (key length: {length} bytes)')
    return key