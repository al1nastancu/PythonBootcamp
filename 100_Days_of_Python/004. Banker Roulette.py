# Who will pay the bill

print("Let's see who pays the bill today!")

names_string = input("Provide everybody's names, separated by a comma.\nNames: ")
names = names_string.split(", ")

import random
x = len(names)  # number of items in list

random_choice = random.randint(0, x-1)
print(names[random_choice] + " is going to pay the bill today!")

# for i in range(len(names)):
#     print(random.choice(names) + " is going to pay the bill today!")
#     break
