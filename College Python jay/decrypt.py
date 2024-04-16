def caesar_cipher_decrypt(encrypted_text, distance):
    decrypted_text = ''
    for char in encrypted_text:
        if char.isprintable():
            decrypted_char = chr((ord(char) - 32 - distance) % 95 + 32)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Input the encrypted text and distance value from the user
encrypted_text = input("Enter the encrypted text: ")
distance = int(input("Enter the distance value: "))

# Call the decryption function
decrypted_text = caesar_cipher_decrypt(encrypted_text, distance)

# Print the decrypted text
print("Decrypted text:", decrypted_text)
