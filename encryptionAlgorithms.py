import string

def encrypt(plain, key, showSteps=False, compareFiles=False):
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + ' ' + '\t' + '\n'
    encrypted_text = ""
    key_index = 0

    for char in plain:
        if char in alphabet:
            shift = alphabet.index(key[key_index % len(key)]) % len(alphabet)
            encrypted_char = alphabet[(alphabet.index(char) + shift) % len(alphabet)]
            
            if showSteps:
                print(f"active_char ({key[key_index % len(key)]}) => {encrypted_char}")
            
            encrypted_text += encrypted_char
            key_index += 1
        else:
            encrypted_text += char
        
    if showSteps:
        print("======================================")
    return encrypted_text


def decrypt(encrypted, key, showSteps=False, compareFiles=False):
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + ' ' + '\t' + '\n'
    decrypted_text = ""
    key_index = 0

    for char in encrypted:
        if char in alphabet:
            shift = alphabet.index(key[key_index % len(key)]) % len(alphabet)
            decrypted_char = alphabet[(alphabet.index(char) - shift) % len(alphabet)]
            
            if showSteps:
                print(f"active_char ({key[key_index % len(key)]}) => {decrypted_char}")
            
            decrypted_text += decrypted_char
            key_index += 1
        else:
            decrypted_text += char
        
    if showSteps:
        print("======================================")
    return decrypted_text