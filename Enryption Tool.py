import string
import os
import time
from colorama import Fore, Back, init


"""
Abailable Bugs ...

-> Ambiguity in Produced Files Naming Logic
"""


def encrypt(plain, key, showSteps=False):
	alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + ' '
	encrypted_text = ""
	key_index = 0

	for char in plain:
		if char in alphabet:
			shift = alphabet.index(key[key_index % len(key)])
			encrypted_char = alphabet[(alphabet.index(char) + shift) % len(alphabet)]
			
			if showSteps == True:
				print("active_char (", key[key_index % len(key)], ") => ", encrypted_char, end='\n')
			
			encrypted_text += encrypted_char
			key_index += 1


		else:
			encrypted_text += char
		
	return encrypted_text


def dycrypt(encrypted, key):
	alphabet = string.ascii_lowercase + string.ascii_letters + string.digits + string.punctuation + ' '
	dycrypted_text = ''
	key_index = 0

	for char in encrypted:
		if char in alphabet:
			shift = alphabet.index(key[key_index % len(key)])
			dycrypted_char = alphabet[(alphabet.index(char) - shift) % len(alphabet)]
			dycrypted_text += dycrypted_char
			key_index += 1
		
		else:
			dycrypted_text += char

	return dycrypted_text


def test_encrypt_decrypt(plain_text, key, showSteps=False):
	encrypted = encrypt(plain_text, key, showSteps)
	print("Decrypted Message Is : ", encrypted)

	decrypted = dycrypt(encrypted, key)
	print("Decrypted Message Is : ", decrypted)

	if (plain_text == decrypted):
		print("successful testing...!")
	else:
		print("Flag Error in the processes...!")


def clear_screen(seconds):
    time.sleep(seconds)
    
    if os.name == 'nt': 	# Windows system
        os.system('cls')
    else:
        os.system('clear')	# UNIX systems


def main():
	init(autoreset=True)

	jump_to_selections = False # Operation Choice (Default)
	jump_to_detection = False  # File Detection	  (Default)
	last_password = ""

	while(True):
		if jump_to_detection == False: # no needing to start from detecting a file
			print (Fore.RED +"\nFor Successful Operation, Put Your File In Path (D:\ ), Firstly")
			if (last_password != ""):
				print (Back.BLUE + "Latest Operation Password", last_password)

			print (Back.BLACK + "1. Encrypt\n2. Decrypt\n3. Quit")
			print (Back.GREEN + "Select a Choice")
			selector = input()

			if(selector in ['1', '2', '3']):
				jump_to_selections = False # Reset Selections Flag
				
				if (selector == '3'):
					print (Fore.BLUE + Back.BLACK + "Quitted ...!")
					quit()

			else:
				print (Back.RED + "Selection Error, choose again ...!")
				jump_to_selections = True # needing to start from Selections

			if jump_to_selections == True: # needing to start from Selections
				continue

		print (Back.GREEN + "\nEnter File Name")
		fileName = input ()

		path = os.path.join("D:\\", fileName)
		if os.path.isfile(path):	
			if (selector == "1"):
				with open(path, 'r') as file:
					fileContent = file.read()

				print (Back.GREEN + "\nChoose a strong password and remember it")
				last_password = key = input()

				encrypted_text = encrypt(fileContent, key)

				if path != f"D:\\Decrypted_{fileName}": # D:\Decrypted_a.txt => fileName = Decrypted_a.txt
					with open(f"D:\\Encrypted_{fileName[10:]}", 'w') as enc_file:
						enc_file.write(encrypted_text)

				else:
					with open(f"D:\\Encrypted_{fileName}", 'w') as enc_file:
						enc_file.write(encrypted_text)

				print (Fore.BLUE + "Successful Encyrption ...!\nPick up the Encrypted File at the same Path.")
				jump_to_detection = False # Reset File Detection Flag
				os.system("Sleep(3000)")
				clear_screen(3)
				
			elif(selector == "2"):
				with open(path, 'r') as file:
					fileContent = file.read()

				print (Back.GREEN + "\nPut you password")
				last_password = key = input()
					
				decrypted_text = dycrypt(fileContent, key)

				if path != f"D:\\Encrypted_{fileName}": # D:\Encyrpted_a.txt => fileName = Encrypted_a.txt
					with open(f"D:\\Decrypted_{fileName[10:]}", 'w') as dec_file:
						dec_file.write(decrypted_text)

				else:
					with open(f"D:\\Decrypted_{fileName}", 'w') as dec_file:
						dec_file.write(decrypted_text)
						
				print (Fore.BLUE + "Successful Decryption ...!\nIf there is an error, check your Password again.")
				jump_to_detection = False # Reset File Detection Flag
				os.system("Sleep(3000)")
				clear_screen(3)
				
		else:
			print(Back.RED + "This File Is Not In The Path ...!")
			jump_to_detection = True # needing to start from detecting a file
	

main()