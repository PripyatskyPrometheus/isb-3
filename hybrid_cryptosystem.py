import argparse
import logging

SETTINGS_FILE = 'files/settings.json'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-set', '--settings', type=str, help='Позволяет использовать  json-файл с указанием необходимых путей для работы системы (Введите путь к файлу)')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', type=int, help='Запускает режим генерации ключей (Введите длину ''симметричного ключа или от 4 до 56 байт (от 32 до 448 бит))')
    group.add_argument('-enc', '--encryption', help='Запускает режим шифрования', action ='store_true')
    group.add_argument('-dec', '--decryption', help='Запускает режим дешифрования', action ='store_true')
    args = parser.parse_args()
