# 100 Days of code by Angela Yu
# Day 8 - Ceasar Cipher

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

direction = input("Type 'e' to encryte, type 'd' to decrypt: ").lower()
text = input("Type your Message: ").lower()
shift = int(input("Type a shift number: "))

message = ""

if direction == "e":
    for letter in text:
        encrypt_index = alphabet.index(letter) + shift

        if encrypt_index > 26:
            encrypt_index = encrypt_index - 26

        message = message + alphabet[encrypt_index]


if direction == "d":
    for letter in text:
        encrypt_index = alphabet.index(letter) - shift

        message = message + alphabet[encrypt_index]


print(message)