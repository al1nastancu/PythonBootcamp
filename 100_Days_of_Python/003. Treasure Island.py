print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
print("LET'S SEE IF YOU CAN FIND THE TREASURE.\n")

location = input("FIRST. You will go: left or right?\nChoice = ")
if location == 'right' or location == 'Right':
    print("---> You stepped in fire! GAME OVER.")
elif location == 'left' or location == 'Left':
    location = input("THERE'S A RIVER ! Would you like to swim or wait?\nChoice = ")
    if location == 'swim' or location == 'Swim':
        print("---> AWWWR, THAT GOLDEN FISH JUST ATE YOU! Game over.")
    elif location == 'wait' or location == 'Wait':
        print("Knock, knock! There are many doors to succes.")
        location = input("You will enter the BLUE one, the RED one or the YELLOW one.\nChoice = ")
        if location == 'blue':
            print("You stepped in a parallel universe. Game over!")
        elif location == 'red':
            print("You turned into a turtle. Sorry, buddy!")
        else:
            print("GOOD Choices, mate! HERE'S YOUR TREASURE:")
            print(''' *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')