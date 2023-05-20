import logging

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

logger = logging.getLogger()
logger.setLevel('INFO')


def generate_asymmetric_keys() -> tuple:
    keys = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    private_key = keys
    public_key = keys.public_key()
    logging.info(f' Asymmetric keys successfully generated')
    return private_key, public_key

def asymmetric_encrypt(public_key, text: bytes) -> bytes:
    cipher_text = public_key.encrypt(text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    logging.info(' Asymmetric encryption was successful')
    return cipher_text