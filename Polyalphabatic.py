def encrypt(plain_text, key):
    encrypted_text = ""
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].upper()) - ord('A')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text += encrypted_char
            key_index += 1
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(encrypted_text, key):
    decrypted_text = ""
    key_index = 0

    for char in encrypted_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].upper()) - ord('A')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted_text += decrypted_char
            key_index += 1
        else:
            decrypted_text += char

    return decrypted_text


# Take input from the user
plain_text = input("Enter the plain text: ")
key = input("Enter the key: ")

# Encrypt the plain text
encrypted_text = encrypt(plain_text, key)
print("Encrypted text:", encrypted_text)

# Decrypt the encrypted text
decrypted_text = decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
