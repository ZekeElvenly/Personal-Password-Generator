from os.path import isfile
import random, secrets, os

def fileChecker():
    filepath = 'dbase.db'
    if os.path.isfile(filepath):
        print('File Exist')
    else:
        print('File does not exist')

def generateKey():
    random_hex = secrets.token_hex(32)
    return random_hex

def passwordGenerator():
	characters = r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&amp;*1234567890"
	passLength = int(12)
	password = ""
	for i in range(passLength):
		password += random.choice(characters)
	return password

def encrypt(text, key):
    encrypted_text = ""
    for i, char in enumerate(text):
        key_char = key[i % len(key)]
        encrypted_text += chr(ord(char) + ord(key_char) % 256)
    return encrypted_text

def decrypt(encrypted_text, key):
    plain_text = ""
    for i, char in enumerate(encrypted_text):
        key_char = key[i % len(key)]
        plain_text += chr(ord(char) - ord(key_char) % 256)
    return plain_text

# Contoh Penggunaan
plain_text = "Hello, world!"
key = generateKey()
print(key)

encrypted_text = encrypt(plain_text, key)
print("Encrypted Text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)

fileChecker()
