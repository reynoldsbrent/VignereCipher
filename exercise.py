import math

# Get the input text to be encrypted from the user
clear_text = input("Which text should be encrypted: ")
# Get the keyword to be used for encryption from the user
keyword = input("Which keyword should be used: ")

# Lists to store individual letters of the text and keyword
word_list = []
keyword_list = []
# List to store the keyword letters that correspond to each letter in the text
keys = []
# List to store the encrypted letters
encrypted_text = []

# List of alphabet letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# List to store calculated shifts for each letter in the text
shifts = []

# Function to encrypt the text using the keyword
def encrypt_text(text, key_word):
    encrypted_string = ""

    # Populate the word_list with individual letters of the text
    for letter in text.lower():
        word_list.append(letter)
    
    # Populate the keyword_list with individual letters of the keyword
    for character in key_word.lower():
        keyword_list.append(character)

    count = 0
    letter_count = 0
    # Match each letter of the text with a letter from the keyword
    while count < len(word_list):
        if letter_count == len(keyword_list):
            letter_count = 0
            keys.append(keyword_list[letter_count])
        else:
            keys.append(keyword_list[letter_count])
        count += 1
        letter_count += 1
    
    # Calculate shifts for each keyword letter
    for key in keys:
       shift = calculate_shifts(key)
       shifts.append(shift)
    count = 0
    # Encrypt each letter of the text
    for letter in word_list:
        if word_list.index(letter) == len(shifts):
            count = 0
        encrypted = encrypt_letter(letter, shifts[count])
        encrypted_text.append(encrypted)
        count += 1
    
    # Build the encrypted string from the list of encrypted letters
    for letter in encrypted_text:
        encrypted_string = encrypted_string + f"{letter}"
    
    return encrypted_string

# Function to encrypt a single letter using a shift value
def encrypt_letter(character, shift):
    letter = ''
    if character not in alphabet:
        letter = character
    elif (alphabet.index(character) + shift) <= 25:
        letter = alphabet[alphabet.index(character) + shift]
    else:
        letter = alphabet[(alphabet.index(character) + shift) - 26]
    return letter

# Function to calculate the shift value based on a keyword letter
def calculate_shifts(letter):
    shift = alphabet.index(letter)
    return shift

# Call the encrypt_text function and print the encrypted result
print(encrypt_text(clear_text, keyword))
