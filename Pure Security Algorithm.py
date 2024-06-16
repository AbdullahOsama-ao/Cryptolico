import string

def encrypt(plain, key):
	alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + ' '
	encrypted_text = ""
	key_index = 0

	for char in plain:
		if char in alphabet:
			shift = alphabet.index(key[key_index % len(key)])
			encrypted_char = alphabet[(alphabet.index(char) + shift) % len(alphabet)]
			
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

def main():
	plain = input("Enter your text, please: ")
	key = input("Enter key of the text, please: ")

	encrypted_text = encrypt(plain, key)
	print("Ecrypted Message Is : ", encrypted_text)

	decrypted = dycrypt(encrypted_text, key)
	print("Decrypted Message Is : ", decrypted)

main()