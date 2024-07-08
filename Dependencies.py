from encryptionAlgorithms import encrypt, decrypt
import os
from colorama import Fore, Back, init
# import time


def clear_screen(seconds=0):
    input("Press (Enter) to Continue...!")
    if os.name == 'nt': 	# Windows system
        os.system('cls')
    else:
        os.system('clear')	# UNIX systems

    # time.sleep(seconds) 	# another option for waiting


def non_empty_input():
	init(autoreset=True)

	while True:
		user_input = input()

		if user_input != "":
			return user_input
		else:
			print (Back.RED + Fore.WHITE + "The key can't be Empty ...!")


def the_same_file(path, key, selector):

	# Restoring File Content into a String
	with open(path, 'r') as file:
		fileContent = file.read()

	# Encryption Case
	if selector == '1':
		encrypted_text = encrypt(fileContent, key)
		with open(path, 'w') as same_file:
			same_file.write(encrypted_text)
			
		print (Fore.BLUE + Back.BLACK + "Successful Encyrption ...!")
		clear_screen()

	# Decryption Case
	elif selector == '2':
		decrypted_text = decrypt(fileContent, key)
		with open(path, 'w') as same_file:
			same_file.write(decrypted_text)
		
		print (Fore.BLUE + Back.BLACK + "Successful Decryption ...!" + Fore.RED + Back.BLACK + "\nIf Decryption isn't correct, make sure Password again.")
		clear_screen()
	

def a_separated_file(path, key, selector, filePath, fileName):

	# Restoring File Content into a String
	with open(path, 'r') as file:
		fileContent = file.read()

	if selector == '1':
		encrypted_text = encrypt(fileContent, key)

		# File Naming hanling
		if "Encrypted_" in fileName or "Decrypted_" in fileName:
			fileName = fileName[10:]
		with open(f"{filePath}\Encrypted_{fileName}", 'w') as enc_file:
			enc_file.write(encrypted_text)

		print (Fore.BLUE + Back.BLACK + "Successful Encyrption ...!\nPick up the Encrypted File at the same Path.")
		clear_screen()

	if selector == '2':
		decrypted_text = decrypt(fileContent, key)

		# File Naming hanling
		if "Encrypted_" in fileName or "Decrypted_" in fileName:
			fileName = fileName[10:]	
		with open(f"{filePath}\Decrypted_{fileName}", 'w') as dec_file:
			dec_file.write(decrypted_text)

		print (Fore.BLUE + Back.BLACK + "Successful Decryption ...!\nPick up the Decrypted File at the same Path." + Fore.RED + Back.BLACK + "\nIf Decryption isn't correct, make sure Password again.")
		clear_screen()


def save_as():
	print (Back.GREEN + Fore.WHITE + "\nSave As ...?")
	print ("1. The Same File\n2. A Separated File")

	while (True):
		user_input = input()
		if user_input == '1' or user_input == '2':
			return user_input
		else:
			print (Back.RED + Fore.WHITE + "Selection Error, choose again ...!")

