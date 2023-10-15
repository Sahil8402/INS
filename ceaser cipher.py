def encrypt_text(plaintext, n):
    ans = ""
    for i in range(len(plaintext)):
        ch = plaintext[i]
        if ch == " ":
            ans += " "
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)

        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)

    return ans


def decrypt():

    # enter your encrypted message(string) below
    encrypted_message = input(
        "Enter the message i.e to be decrypted: ").strip()

    letters = "abcdefghijklmnopqrstuvwxyz"

    # enter the key value to decrypt
    k = int(input("Enter the key to decrypt: "))
    decrypted_message = ""

    for ch in encrypted_message:

        if ch in letters:
            position = letters.find(ch)
            new_pos = (position - k) % 26
            new_char = letters[new_pos]
            decrypted_message += new_char
        else:
            decrypted_message += ch
    return decrypted_message


plaintext = str(input("Enter Plain Text:-"))
n = int(input("Enter n:-"))
print("Plain Text is : " + plaintext)
print("Shift pattern is : " + str(n))
print("Cipher Text is : " + encrypt_text(plaintext, n))
print(decrypt())
