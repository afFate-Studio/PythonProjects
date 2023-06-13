from random import randint
import pyinputplus as pyip

# word list for the game
word_list = ["aardvark", "baboon", "camel"]

word = word_list[randint(0, len(word_list))] # dynamic randint based on the word_list used to choose a word from the list
game_word = []      # empty list used to keep track of if the user guessed the correct value
user_guesses = [] # empty list to keep track of user guesses

"""
    iterates over the length of the chosen word and then appends the correct amount
    of '_' to game_word list
"""
for i in range(len(word)):
    game_word.append('_') # appends to a list, used to keep track of if the user guessed the correct value
print(''.join(map(str, game_word)))  # shows user the length of the word without showing the word

while True:

    user_guess = pyip.inputStr("Guess a letter: ")[0].lower() # splices user string to first character then makes it lowercase

    """
        checks user guess and then replaces the '_' in game_word with the letter
        if the guess was correct.
    """
    for i in range(len(word)):
        if user_guess == user_guesses[i]:
            print("You have already guessed that.")
        elif user_guess == word[i]:
                game_word[i] = user_guess
        

    print(''.join(map(str, game_word))) # makes the list a single word and prints it