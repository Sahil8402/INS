def encrypt_rail_fence(plaintext, num_rails):
    rail_fence = [['' for _ in range(len(plaintext))]
                  for _ in range(num_rails)]
    rail = 0
    direction = 1
    for char in plaintext:
        rail_fence[rail].append(char)
        rail += direction
        if rail == num_rails - 1 or rail == 0:
            direction = -direction
    ciphertext = ''.join(
        [char for rail in rail_fence for char in rail if char != ''])
    return ciphertext


def decrypt_rail_fence(ciphertext, num_rails):
    rail_fence = [['' for _ in range(len(ciphertext))]
                  for _ in range(num_rails)]
    rail = 0
    direction = 1
# Calculate the pattern of rails
    pattern = []
    for _ in range(len(ciphertext)):
        pattern.append(rail)
        rail += direction
        if rail == num_rails - 1 or rail == 0:
            direction = -direction

    # Write each character of the ciphertext to the appropriate rail
    index = 0
    for char in ciphertext:
        rail_fence[pattern[index]].append(char)
        index += 1

    # Read each rail to get the plaintext
    plaintext = ''.join([char for rail in rail_fence for char in rail])
    return plaintext


# Example usage:
plaintext = "SAHILGANDHI"
num_rails = 11

ciphertext = encrypt_rail_fence(plaintext, num_rails)
decrypted_text = decrypt_rail_fence(ciphertext, num_rails)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)


# def monoatomic_encrypt(text, shift):
#   """Encrypts a string using the monoatomic cipher."""
#   encrypted_text = ""
#   for char in text:
#     encrypted_text += chr(ord(char) + shift)
#   return encrypted_text

# def monoatomic_decrypt(text, shift):
#   """Decrypts a string using the monoatomic cipher."""
#   decrypted_text = ""
#   for char in text:
#     decrypted_text += chr(ord(char) - shift)
#   return decrypted_text

# def main():
#   text = input("Enter the text to encrypt: ")
#   shift = int(input("Enter the shift value: "))
#   encrypted_text = monoatomic_encrypt(text, shift)
#   decrypted_text = monoatomic_decrypt(encrypted_text, shift)

#   print("Original text:", text)
#   print("Encrypted text:", encrypted_text)
#   print("Decrypted text:", decrypted_text)

# if __name__ == "__main__":
#   main()

