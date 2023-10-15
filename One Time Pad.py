def encrypt(plain_text, key):
    encrypted_text = ""
    for i in range(len(plain_text)):
        char = plain_text[i]
        key_char = key[i % len(key)]
        encrypted_char = chr((ord(char) + ord(key_char) - 2 * ord('A')) % 26 + ord('A'))
        encrypted_text += encrypted_char
    return encrypted_text


def decrypt(encrypted_text, key):
    decrypted_text = ""
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        key_char = key[i % len(key)]
        decrypted_char = chr((ord(char) - ord(key_char) + 26) % 26 + ord('A'))
        decrypted_text += decrypted_char
    return decrypted_text


# Take input from the user
plain_text = input("Enter the plain text: ").upper()
key = input("Enter the key: ").upper()

# Encrypt the plain text
cipher_text = encrypt(plain_text, key)
print("Cipher text:", cipher_text)

# Decrypt the encrypted text
decrypted_text = decrypt(cipher_text, key)
print("Message:", decrypted_text)
