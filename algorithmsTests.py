from encryptionAlgorithms import encrypt, decrypt



def test_encrypt_decrypt(plain_text, key, showSteps=False):
	encrypted = encrypt(plain_text, key, showSteps)
	print("Encyrpted Message Is : \n", encrypted)

	decrypted = decrypt(encrypted, key)
	print("Decrypted Message Is : \n", decrypted)

	if (plain_text == decrypted):
		print("successful testing...!")
	else:

		print("Flag Error in the processes...!")



def main_test():
	result = test_encrypt_decrypt("asdlkfal;skd", "here")

	print(result)

