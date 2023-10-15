def encrypt(message, key):
    encrypted_message = ""
    for ch in message:
        encrypted_message += chr(ord(ch) + key)
    return encrypted_message


def decrypt(message, key):
    decrypted_message = ""
    for ch in message:
        decrypted_message += chr(ord(ch) - key)
    return decrypted_message


def main():
    message = input("Enter a message: ")
    key = int(input("Enter a key: "))
    encrypted_message = encrypt(message, key)
    print("Encrypted message: ", encrypted_message)
    decrypted_message = decrypt(encrypted_message, key)
    print("Decrypted message: ", decrypted_message)


main()