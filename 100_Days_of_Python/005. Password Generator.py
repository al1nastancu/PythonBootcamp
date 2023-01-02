# Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?:\n"))
nr_symbols = int(input(f"How many symbols would you like:\n"))
nr_numbers = int(input(f"How many numbers would you like?:\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = " "  # we create a variable as a string
# for char in range(1, nr_letters + 1):
#     random_char = random.choice(letters)  # we pick a random letter from the list "letters"
#     password = password + random_char  # we add it to the string
#
# for char in range(1, nr_symbols + 1):
#     random_char = random.choice(symbols)  # we pick a random symbol from the list "symbols"
#     password += random_char  # we add it to the string
#
# for char in range(1, nr_numbers + 1):
#     random_char = random.choice(numbers)  # we pick a random number from the list "numbers"
#     password += random_char  # we add it to the string
#
# print(f"Your new Password is: {password}")  # it will print the password ordered: letters, symbols, numbers


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []  # we create a list that can be reordered after

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))  # add a random choice from letters

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))  # add a random choice from symbols

for char in range(1, nr_numbers + 1):
    password_list.append((random.choice(numbers)))  # add a random choice from numbers

random.shuffle(password_list)  # randomly reorder the list

password = " "  # create a string for the list elements
for char in password_list:  # go through the list of randomly generated elements
    password += char  # add the elements here

print(password)