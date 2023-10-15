import string
import random

# Define the original and cipher alphabets
original_alphabet = string.ascii_lowercase
cipher_alphabet = list(original_alphabet)
random.shuffle(cipher_alphabet)
cipher_alphabet = ''.join(cipher_alphabet)

# Create a dictionary to map between original and cipher letters
encryption_dict = dict(zip(original_alphabet, cipher_alphabet))
decryption_dict = dict(zip(cipher_alphabet, original_alphabet))

def encrypt(plaintext):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha() and char.islower():
            ciphertext += encryption_dict[char]
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha() and char.islower():
            plaintext += decryption_dict[char]
        else:
            plaintext += char
    return plaintext

# Take input from the user
text_to_encrypt = input("Enter the text to encrypt: ")

encrypted_text = encrypt(text_to_encrypt)
print(f"Encrypted text: {encrypted_text}")

text_to_decrypt = input("Enter the text to decrypt: ")

decrypted_text = decrypt(text_to_decrypt)
print(f"Decrypted text: {decrypted_text}")
