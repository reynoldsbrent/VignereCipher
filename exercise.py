import math

clear_text = input("Which text should be encrypted: ")
keyword = input("Which keyword should be used: ")
word_list = []
keyword_list = []
keys = []
encrypted_text = []
def encrypt_text(text, key_word):
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
       encrypted = encrypt_letter(key, shift)
       encrypted_text.append(encrypted)
    return

def encrypt_letter(character, shift):
    diff = abs(ord(character) - shift)
    return diff


def calculate_shifts(letter):
    shift = ord(letter)
    return shift


print(encrypt_text(clear_text, keyword))