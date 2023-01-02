"""
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.
Let's go!
"""

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("LET'S PLAY!\nRock, Paper, Scissors!")
import random
me = 0
comp = 0

while True:

    move = int(input("0 = Rock, 1 = Paper, 2 = Scissors\nYour move: "))
    if move == 0:
        print(rock)
    elif move == 1:
        print(paper)
    else:
        print(scissors)

    moves = ["rock", "paper", "scissors"]
    computer = random.randint(0,len(moves)-1)

    if move == 0 and moves[computer] == "paper":
        print("COMPUTER:")
        print(paper)
        print("---> You lose.")
        comp += 1
    elif move == 1 and moves[computer] == "scissors":
        print("COMPUTER:")
        print(scissors)
        print("---> You lose.")
        comp += 1
    elif move == 2 and moves[computer] == "rock":
        print("COMPUTER:")
        print(rock)
        print("---> You lose.")
        comp += 1
    elif move == 0 and moves[computer] == "rock":
        print("COMPUTER:")
        print(rock)
        print("---> Draw!")
        comp += 1
        me += 1
    elif move == 1 and moves[computer] == "paper":
        print("COMPUTER:")
        print(paper)
        print("---> Draw!")
        comp += 1
        me += 1
    elif move == 2 and moves[computer] == "scissors":
        print("COMPUTER:")
        print(scissors)
        print("---> Draw!")
        comp += 1
        me += 1
    else:
        print("COMPUTER:")
        if moves[computer] == "rock":
            print(rock)
        elif moves[computer] == "paper":
            print(paper)
        else:
            print(scissors)
        print("---> Congrats! You're the WINNER!")
        me += 1
    print(f"The SCORE is {me} for you and {comp} for the computer!\n")
    if me == 3:
        print("The User WON!")
    elif comp == 3:
        print("The Computer WON!")

    if me == 3 or comp == 3:
        break