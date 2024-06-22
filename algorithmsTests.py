from encryptionAlgorithms import encrypt, decrypt


def test_encrypt_decrypt(plain_text, key, showSteps=False, compareFiles=False):
	encrypted = encrypt(plain_text, key, showSteps)
	decrypted = decrypt(encrypted, key, showSteps)

	if (plain_text == decrypted):
		print("successful testing...!")
	else:
		print("Flag Error in the processes...!")

	if (compareFiles == True):
		print("Encyrpted Message Is:\n", encrypted, "\n")
		print("Decrypted Message Is:\n", decrypted, "\n")


def main_test():
	test_encrypt_decrypt("plain_text_here", "key_here", True, True)

if __name__ == "__main_test__":
	main_test()