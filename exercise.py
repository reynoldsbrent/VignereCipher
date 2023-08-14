import math

clear_text = input("Which text should be encrypted: ")
keyword = input("Which keyword should be used: ")
word_list = []
keyword_list = []
keys = []
encrypted_text = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
shifts = []
def encrypt_text(text, key_word):
    encrypted_string = ""

    for letter in text.lower():
        word_list.append(letter)
    
    for character in key_word.lower():
        keyword_list.append(character)

    count = 0
    letter_count = 0
    while count < len(word_list):
        if letter_count == len(keyword_list):
            letter_count = 0
            keys.append(keyword_list[letter_count])
        else:
            keys.append(keyword_list[letter_count])
        count += 1
        letter_count += 1
    
    for key in keys:
       shift = calculate_shifts(key)
       shifts.append(shift)
    count = 0
    for letter in word_list:
        if word_list.index(letter) == len(shifts):
            count = 0
        #encrypted = encrypt_letter(letter, shifts[word_list.index(letter)])
        encrypted = encrypt_letter(letter, shifts[count])
        encrypted_text.append(encrypted)
        count += 1
    
    
    for letter in encrypted_text:
        encrypted_string = encrypted_string + f"{letter}"
    
    return encrypted_string

def encrypt_letter(character, shift):
    letter = ''
    if character not in alphabet:
        letter = character
    elif (alphabet.index(character) + shift) <= 25:
        letter = alphabet[alphabet.index(character) + shift]
    else:
        letter = alphabet[(alphabet.index(character) + shift) - 26]
    return letter


def calculate_shifts(letter):
    shift = alphabet.index(letter)
    return shift


print(encrypt_text(clear_text, keyword))