import logging
import json

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key

logger = logging.getLogger()
logger.setLevel('INFO')

def load_settings(settings_file: str) -> dict:
    settings_data = None
    try:
        with open(settings_file) as json_file:
            settings_data = json.load(json_file)
        logging.info(f"Settings file successfully loaded from file {settings_file}")
    except OSError as err:
        logging.warning(f"Settings file was not loaded from file {settings_file}\n{err}")
    return settings_data

def save_asymmetric_keys(private_key, public_key, private_pem: str, public_pem: str) -> None:
    try:
        with open(private_pem, 'wb') as private_out:
            private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                        encryption_algorithm=serialization.NoEncryption()))
        logging.info(f' Private key successfully saved to {private_pem}')
    except OSError as err:
        logging.warning(f' Private key was not saved to file {private_pem}\n{err}')
    try:
        with open(public_pem, 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))
        logging.info(f' Public key successfully saved to {public_pem}')
    except OSError as err:
        logging.warning(f' Public key was not saved to file {public_pem}\n{err}')

def save_symmetric_key(key: bytes, file_name: str) -> None:
    try:
        with open(file_name, 'wb') as key_file:
            key_file.write(key)
        logging.info(f' Symmetric key successfully saved to {file_name}')
    except OSError as err:
        logging.warning(f' Symmetric key was not saved to file {file_name}\n{err}')