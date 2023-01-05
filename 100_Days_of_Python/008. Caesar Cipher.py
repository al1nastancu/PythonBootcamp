alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
'''
we make a double list for the alphabet so that it could 
work for letters like y, z to not be out of range when shifted 
'''

# METHOD 1 - with separate functions

# def encypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:  # for each letter in the initial word
#         position = alphabet.index(letter)  # we search for its index in the alphabet
#         new_position = position + shift_amount  # indentify the new position
#         new_letter = alphabet[new_position]  # indentify the new letter
#         cipher_text += new_letter  # replace the letter by adding it to a new str cipher_text
#     print(f"The encrypted word is {cipher_text}")
#
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"The decrypted word is '{cipher_text}' ")
#
# stop = False
#
# while stop == False:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
#     text = input("Type your message: \n").lower()
#     shift = int(input("Type the shift number: \n"))
#
#     if direction != 'encode' and direction != 'decode':  # check exception
#         print("Please insert only encode / decode")
#     elif direction == 'encode':
#         encypt(plain_text= text, shift_amount= shift)  # call functions
#     else:
#         decrypt(cipher_text=text,shift_amount=shift)
#
#     print("Would you like to encode/decode another word? Yes/No : ")
#     choice = input().lower()
#     if choice == 'no':
#         stop = True  # this is when the algoritm stops


# METHOD 2 - 1 function called caesar()

# def caesar(text, shift_choice, direction):
#     new_text = ''
#     for letter in text:
#         position = alphabet.index(letter)
#         if direction != 'encode' and direction != 'decode':  # check exception
#             print("Please insert only encode / decode")
#         elif direction == 'encode':
#             new_position = position + shift_choice
#             new_letter = alphabet[new_position]
#             new_text += new_letter
#         else:
#             new_position = position - shift_choice
#             new_letter = alphabet[new_position]
#             new_text += new_letter
#
#     print(f"The result is '{new_text}' ")

# METHOD 2 - BETTER
def caesar(text, shift_choice, direction):
    new_text = ''
    for letter in text:
        if direction != 'encode' and direction != 'decode':  # check exception
            print("Please insert only encode / decode")
        elif shift_choice > 26:
            print("Please provide a shift < 26.")
        else:
            if letter.isalpha() == True:
                if direction == 'decode':
                    shift_choice *= -1
                position = alphabet.index(letter)
                new_position = position + shift_choice
                new_letter = alphabet[new_position]
                new_text += new_letter
            else:
                new_text += letter
    print(f"The result is '{new_text}' ")

stop = False

while stop == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    caesar(text, shift, direction)

    print("Would you like to encode/decode another word? Yes/No : ")
    choice = input().lower()
    if choice == 'no':
        stop = True  # this is when the algoritm stops