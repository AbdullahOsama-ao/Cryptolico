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
		

def main():
	init(autoreset=True)

	jump_to_choice_only = False # Operation Choice	  (Directly)
	jump_to_file_detec = False  # Directory Detection (Directly)
	jump_to_dir_detec = False 	# File Detection	  (Directly)	
	jump_to_key = False			# Key Input			  (Directly)	
	# last_password = ""		# The Last Procees Password

	while(True):

		# No Need to jump to Enter a Choice Directly
		if jump_to_choice_only == False:
			print (Back.BLACK + Fore.WHITE + "1. Encrypt\n2. Decrypt\n3. Quit")
			print (Back.GREEN + Fore.WHITE + "Select a Choice")
			jump_to_choice_only = True
		
		# No Need to start from Detecting a File or a Directory Directly
		if jump_to_dir_detec == False and jump_to_file_detec == False:

			# if (last_password != ""):
			# 	print (Back.BLUE + Fore.WHITE + "Latest Operation Password", last_password)

			# Handling Code Running Life
			selector = input()
			if(selector in ['1', '2', '3']):
				if (selector == '3'):
					print (Fore.BLUE + Back.BLACK + "Quitted ...!")
					quit()		
			else:
				print (Back.RED + Fore.WHITE + "Selection Error, choose again ...!")
				continue

			print (Back.GREEN + Fore.WHITE + "\nPaste Directory Path")
			jump_to_dir_detec = True

		# Need to jump to Directory Detection Directly
		if jump_to_dir_detec == True and jump_to_key == False:
			filePath = input ()
			filePath = filePath.strip('"')
			filePath = filePath.strip("'")

			# Directory Is not Exist on The Device
			if not os.path.isdir(filePath):
				jump_to_dir_detec = True
				print(Back.RED + Fore.WHITE + "Directory Path Isn't Exist, Copy and Paste it again ...!")
				continue

			print (Back.GREEN + Fore.WHITE + "\nEnter File Name")

		# No Need to jump to Enter a Key Directly
		if jump_to_key == False:
			fileName = input ()

			path = filePath
			root_dir = os.listdir(path)
			# Looping Over All Files in The Directory Path
			for each_file in root_dir:

				file_name_in_dir, file_in_dir_ext = os.path.splitext(each_file) # each_file = name + extenstion
				
				# Handling The File Name With File Extension
				if fileName == file_name_in_dir or fileName == file_name_in_dir+file_in_dir_ext:
					path = os.path.join(filePath, each_file)
					if fileName == file_name_in_dir:
						fileName = each_file

					# Add-ons
					print (Back.BLUE + Fore.WHITE + path + Back.WHITE + Fore.BLUE + " Ready!")
					if selector == '1':
						print (Back.GREEN + Fore.WHITE + "\nChoose a strong password and remember it")
					elif selector == '2':
						print (Back.GREEN + Fore.WHITE + "\nPut your password")

		# File Is Found In The Directory
		if os.path.isfile(path):

			if selector == "1":

				# Restoring File Content into a String
				with open(path, 'r') as file:
					fileContent = file.read()
				
				# Key Input handling before Algorithm Calculations
				key = input()
				if key == "":
					print (Back.RED + Fore.WHITE + "The key can't be Empty ...!")
					jump_to_key = True
					continue
				encrypted_text = encrypt(fileContent, key)

				# File Naming hanling
				if "Encrypted_" in fileName or "Decrypted_" in fileName: # D:\Decrypted_a.txt => fileName = Decrypted_a.txt
					fileName = fileName[10:]
				with open(f"{filePath}\Encrypted_{fileName}", 'w') as enc_file:
					enc_file.write(encrypted_text)


				print (Fore.BLUE + Back.BLACK + "Successful Encyrption ...!\nPick up the Encrypted File at the same Path.")
				
				# Jumping Flags Resetting
				jump_to_choice_only = False
				jump_to_dir_detec = False
				jump_to_file_detec = False # Reset File Detection Flag
				jump_to_key = False
				clear_screen()

			if selector == "2":

				# Restoring File Content into a String
				with open(path, 'r') as file:
					fileContent = file.read()

				# Key Input handling before Algorithm Calculations
				key = input()
				if key == "":
					print (Back.RED + Fore.WHITE + "The key can't be Empty ...!")
					jump_to_key = True
					continue
				decrypted_text = decrypt(fileContent, key)

				# File Naming hanling
				if "Encrypted_" in fileName or "Decrypted_" in fileName:
					fileName = fileName[10:]	
				with open(f"{filePath}\Decrypted_{fileName}", 'w') as dec_file:
					dec_file.write(decrypted_text)

				print (Fore.BLUE + Back.BLACK + "Successful Decryption ...!\nIf Decryption isn't correct, make sure Password again.")
				
				# Jumping Flags Resetting
				jump_to_choice_only = False # Enter Choice
				jump_to_dir_detec = False	# Directory Detection
				jump_to_file_detec = False 	# File Detection
				clear_screen()
		
		# File Is not Found In The Directory
		else:
			print(Back.RED + Fore.WHITE + "This File Isn't Exist, Enter File Name again ...!")
			jump_to_dir_detec = False
			jump_to_file_detec = True 		# needing to start from detecting a file


if __name__ == "__main__":
	main()
