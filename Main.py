from encryptionAlgorithms import encrypt, decrypt
from algorithmsTests import test_encrypt_decrypt
import os
import time
from colorama import Fore, Back, init


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
	jump_to_dir_detec = False # File Detection		  (Directly)	
	# last_password = ""

	while(True):
		if jump_to_choice_only == False:
			print (Back.BLACK + Fore.WHITE + "1. Encrypt\n2. Decrypt\n3. Quit")
			jump_to_choice_only = True
		
		if jump_to_dir_detec == False and jump_to_file_detec == False: # no needing to start from detecting a file
			# if (last_password != ""):
			# 	print (Back.BLUE + Fore.WHITE + "Latest Operation Password", last_password)

			print (Back.GREEN + Fore.WHITE + "Select a Choice")
			selector = input()

			if(selector in ['1', '2', '3']):
				if (selector == '3'):
					print (Fore.BLUE + Back.BLACK + "Quitted ...!")
					quit()

			else:
				print (Back.RED + Fore.WHITE + "Selection Error, choose again ...!")
				continue

			jump_to_dir_detec = True

		if jump_to_dir_detec == True:
			print (Back.GREEN + Fore.WHITE + "\nPaste Directory Path")
			filePath = input ()
			filePath = filePath.strip('"')
			filePath = filePath.strip("'")

			if not os.path.isdir(filePath):
				jump_to_dir_detec = True
				print(Back.RED + Fore.WHITE + "Directory Path Isn't Exist At Your Device ...!")
				continue
		

		print (Back.GREEN + Fore.WHITE + "\nEnter File Name")
		fileName= input ()
		
		if ".txt" not in fileName:
			fileName = fileName + ".txt"

		path = os.path.join(filePath, fileName)
		

		if os.path.isfile(path):	
			print (Back.BLUE + Fore.WHITE + path + Back.WHITE + Fore.BLUE + " Ready!")
			if (selector == "1"):
				with open(path, 'r') as file:
					fileContent = file.read()

				print (Back.GREEN + Fore.WHITE + "\nChoose a strong password and remember it")
				key = input()

				encrypted_text = encrypt(fileContent, key)

				if "Encrypted_" in fileName or "Decrypted_" in fileName: # D:\Decrypted_a.txt => fileName = Decrypted_a.txt
					fileName = fileName[10:]

				with open(f"{filePath}\Encrypted_{fileName}", 'w') as enc_file:
					enc_file.write(encrypted_text)

				# if path != f"D:\\Decrypted_{fileName}": # D:\Decrypted_a.txt => fileName = Decrypted_a.txt
				# 	with open(f"D:\\Encrypted_{fileName[10:]}", 'w') as enc_file:
				# 		enc_file.write(encrypted_text)

				# else:
				# 	with open(f"D:\\Encrypted_{fileName}", 'w') as enc_file:
				# 		enc_file.write(encrypted_text)
				#-------------------------------
				# with open(f"{filePath}Encrypted_File.txt", 'w') as enc_file:
				# 		enc_file.write(encrypted_text)

				print (Fore.BLUE + Back.BLACK + "Successful Encyrption ...!\nPick up the Encrypted File at the same Path.")
				jump_to_choice_only = False
				jump_to_dir_detec = False
				jump_to_file_detec = False # Reset File Detection Flag
				clear_screen()
				
			elif(selector == "2"):
				with open(path, 'r') as file:
					fileContent = file.read()

				print (Back.GREEN + Fore.WHITE + "\nPut your password")
				key = input()
					
				decrypted_text = decrypt(fileContent, key)

				if "Encrypted_" in fileName or "Decrypted_" in fileName: # D:\Encyrpted_a.txt => fileName = Encrypted_a.txt
					fileName = fileName[10:]
					
				with open(f"{filePath}\Decrypted_{fileName}", 'w') as dec_file:
					dec_file.write(decrypted_text)

				# if path != f"D:\\Encrypted_{fileName}": # D:\Encyrpted_a.txt => fileName = Encrypted_a.txt
				# 	with open(f"D:\\Decrypted_{fileName[10:]}", 'w') as dec_file:
				# 		dec_file.write(decrypted_text)

				# else:
				# 	with open(f"D:\\Decrypted_{fileName}", 'w') as dec_file:
				# 		dec_file.write(decrypted_text)
				#----------------------------------
				# with open(f"{filePath}Decrypted_File.txt", 'w') as dec_file:
				# 		dec_file.write(decrypted_text)
						
				print (Fore.BLUE + Back.BLACK + "Successful Decryption ...!\nIf Decryption isn't correct, make sure Password again.")
				jump_to_choice_only = False
				jump_to_dir_detec = False
				jump_to_file_detec = False # Reset File Detection Flag
				clear_screen()
						
		else:
			print(Back.RED + Fore.WHITE + "This File Is Not In The Path ...!")
			jump_to_dir_detec = False
			jump_to_file_detec = True # needing to start from detecting a file


if __name__ == "__main__":
	main()
