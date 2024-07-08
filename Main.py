from encryptionAlgorithms import encrypt, decrypt
from Dependencies import the_same_file, a_separated_file, save_as, non_empty_input
import os
from colorama import Fore, Back, init


def main():
	init(autoreset=True)

	jump_to_choice_only = False # Operation Choice	  (Directly)
	jump_to_file_detec = False  # Directory Detection (Directly)
	jump_to_dir_detec = False 	# File Detection	  (Directly)	
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
					return 0
			else:
				print (Back.RED + Fore.WHITE + "Selection Error, choose again ...!")
				continue

			print (Back.GREEN + Fore.WHITE + "\nPaste Directory Path")
			jump_to_dir_detec = True

		# Need to jump to Directory Detection Directly
		if jump_to_dir_detec == True:
			filePath = input ()
			filePath = filePath.strip('"')
			filePath = filePath.strip("'")

			# Directory Is not Exist on The Device
			if not os.path.isdir(filePath):
				jump_to_dir_detec = True
				print(Back.RED + Fore.WHITE + "Directory Path Isn't Exist, Copy and Paste it again ...!")
				continue

			print (Back.GREEN + Fore.WHITE + "\nEnter File Name")
		
		fileName = input ()
		path = filePath
		root_dir = os.listdir(path)
		# Looping Over All Files in The Directory Path
		for each_file in root_dir:
			file_name_in_dir, file_in_dir_ext = os.path.splitext(each_file) # each_file = name + extenstion
			
			# File Is Found In The Directory (handle file name & file extension)
			if fileName == file_name_in_dir or fileName == file_name_in_dir+file_in_dir_ext:
				path = os.path.join(filePath, each_file)
				if fileName == file_name_in_dir:
					fileName = each_file
				print (Back.BLUE + Fore.WHITE + path + Back.WHITE + Fore.BLUE + " Ready!")

				# Check Selector Encryption/Decryption
				if selector == '1':
					print (Back.GREEN + Fore.WHITE + "\nChoose a strong password and remember it")
				elif selector == '2':
					print (Back.GREEN + Fore.WHITE + "\nPut your password")
				# Key must be non-Empty
				key = non_empty_input()

		# File Is not Found In The Directory	
		if not os.path.isfile(path):
			print(Back.RED + Fore.WHITE + "This File Isn't Exist, Enter File Name again ...!")
			jump_to_dir_detec = False
			jump_to_file_detec = True 	# needing to start from detecting a file
			continue

		# How To Save
		the_same_file(path, key, selector) if save_as() == '1' else a_separated_file(path, key, selector, filePath, fileName)
		# Jumping Flags Resetting
		jump_to_choice_only = False # Enter Choice
		jump_to_dir_detec = False	# Directory Detection
		jump_to_file_detec = False 	# File Detection


if __name__ == "__main__":
	main()
