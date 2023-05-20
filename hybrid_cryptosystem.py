import argparse
import logging

from system_functen import load_settings, save_asymmetric_keys, save_symmetric_key
from symmetric_encyption import generate_symmetric_key
from asymmetric_encyption import generate_asymmetric_keys, asymmetric_encrypt

SETTINGS_FILE = 'files/settings.json'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-set', '--settings', type=str, help='Позволяет использовать  json-файл с указанием необходимых путей для работы системы (Введите путь к файлу)')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', type=int, help='Запускает режим генерации ключей (Введите длину ''симметричного ключа или от 4 до 56 байт (от 32 до 448 бит))')
    group.add_argument('-enc', '--encryption', help='Запускает режим шифрования', action ='store_true')
    group.add_argument('-dec', '--decryption', help='Запускает режим дешифрования', action ='store_true')
    args = parser.parse_args()
    settings = load_settings(args.settings) if args.settings else load_settings(SETTINGS_FILE)
    if settings:
         if args.generation:
            length = args.generation
            if 4 <= length <= 56:
                symmetric_key = generate_symmetric_key(length)
                private_key, public_key = generate_asymmetric_keys()
                save_asymmetric_keys(private_key, public_key, settings['secret_key'], settings['public_key'])
                cipher_symmetric_key = asymmetric_encrypt(public_key, symmetric_key)
                save_symmetric_key(cipher_symmetric_key, settings['symmetric_key'])
            else:
                logging.warning('Symmetric key must be between 4 and 56 bytes long')