from encryptionAlgorithms import encrypt, decrypt
from colorama import Fore, Back, init


def test_encrypt_decrypt(plain_text, key, showSteps=False, compareFiles=False):
	init(autoreset=True)
	encrypted = encrypt(plain_text, key, showSteps)
	decrypted = decrypt(encrypted, key, showSteps)

	if (plain_text == decrypted):
		print(Back.GREEN + Fore.WHITE + "successful Process...!")
	else:
		print(Back.Red + Fore.WHITE + "Flag Error in the processes...!")

	if (compareFiles == True):
		print(Back.BLUE + Fore.WHITE + "Encyrpted Message Is:")
		print(encrypted)

		print(Back.BLUE + Fore.WHITE + "Decrypted Message Is:")
		print(decrypted)


def main_test():
	test_encrypt_decrypt("plain_text_here", "key_here", True, True)


if __name__ == "__main__":
	main_test()