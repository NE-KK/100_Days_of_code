# 100 Days of code by Angela Yu
# Day 82 - Professional Portfolio Project - Morsecode converter

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..',
                    'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 
                    'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..',
                    '9':'----.', '0':'-----', 
                    ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}      

print("Welcome to the Morse Code Converter!")

text_input = input("Enter a word to convert to Morse Code: ").upper()
morse_code_output = ""
for letter in text_input:
    if letter in MORSE_CODE_DICT:
        morse_code_output += MORSE_CODE_DICT[letter] + " "
    else:
        morse_code_output += " "  # For spaces or unrecognized characters   

print(f"The Morse Code for '{text_input}' is: {morse_code_output}")
