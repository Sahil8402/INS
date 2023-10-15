from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad(text):
    while len(text) % 16 != 0:
        text += b' '
    return text

def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad(plaintext)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def aes_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext).rstrip(b' ')
    return plaintext

def main():
    key = get_random_bytes(16)  
    print("Generated Key:", key.hex())
    
    plaintext = input("Enter the plaintext to encrypt: ").encode()
    ciphertext = aes_encrypt(plaintext, key)
    print("Cipher text:", ciphertext.hex())

    decrypted_text = aes_decrypt(ciphertext, key)
    print("Decrypted message:", decrypted_text.decode())

if __name__ == "__main__":
    main()
