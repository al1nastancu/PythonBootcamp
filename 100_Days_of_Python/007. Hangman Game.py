word_list = ['cat', 'dog', 'bird', 'mouse', 'house', 'tree', 'flower', 'grass', 'sky', 'cloud', 'zombie', 'ocean', 'beach', 'desert', 'mountain', 'river', 'lake', 'island', 'apple', 'banana', 'pear', 'grapes', 'strawberry', 'orange', 'lemon', 'lime', 'mango', 'watermelon']

import random
chosen_word = random.choice(word_list)  # chose a random word

# Testing Code, for debugging
# print(f"The word is {chosen_word}")

display = []  # this list will be displayed to the user
for i in range(len(chosen_word)):
    display.append("_")  # create a list with "_"

print(" ".join(display))


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6
letters_tried = []
end_of_game = False
while not end_of_game:  # while we still have "_" in display list
    guess = input("Guess a letter: ").lower()
    if guess not in letters_tried:
        letters_tried.append(guess)
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:  # compare letters guessed <-> letters of the chosen word
                display[i] = guess
                print(f"You guessed letter {guess}. Keep going!")
        if guess not in chosen_word:  # if the letter is not in the chose word,
            lives -= 1  # you lose a life/try
            print(f"Letter {guess} is not in word. You lose a life!")
            if lives == 0:
                end_of_game = True
                print(f"You lose. The word was ---> {chosen_word}!")  # end of game

        print(" ".join(display))

        if "_" not in display:  # this is True when you guessed the word
            end_of_game = True
            print("You guessed all letters in time!")
            print("You win!")
    else:
        print(f"You already tried letter {guess} before!")

    print(stages[lives])  # because the stages are in order of the lives, we can display it

