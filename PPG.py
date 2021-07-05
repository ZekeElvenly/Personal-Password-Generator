import random

def passwordGenerator():
	characters = r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&amp;*1234567890"
	passLength = int(12)
	password = ""
	for i in range(passLength):
		password += random.choice(characters)
	return password


