from random import randint
import pyinputplus as pyip

# word list for the game
word_list = ["aardvark", "baboon", "camel"]

word = word_list[randint(0, len(word_list)-1)] # dynamic randint based on the word_list used to choose a word from the list
game_word = []      # empty list used to keep track of if the user guessed the correct value
user_guesses = [] # empty list to keep track of user guesses
LIVES = 6
"""
    iterates over the length of the chosen word and then appends the correct amount
    of '_' to game_word list
"""
for i in range(len(word)):
    game_word.append('_') # appends to a list, used to keep track of if the user guessed the correct value
print(''.join(map(str, game_word)))  # shows user the length of the word without showing the word

while True:
    PROMPT = pyip.inputStr("Guess a letter: ")[0].lower()
    user_guess = PROMPT # splices user string to first character then makes it lowercase

    """
        checks user guess and then replaces the '_' in game_word with the letter
        if the guess was correct.
    """
    
    if len(user_guesses) != 0:
        for count, var in enumerate(user_guesses):
            if user_guess == user_guesses[count]:
                print('You have already guessed that')
                break

    for count, var in enumerate(word):
        if user_guess == word[count]:
            game_word[count] = user_guess
    user_guesses.append(user_guess)
   
    if ''.join(map(str, game_word)) == word:
        print('You win!')
        break

    else:
        LIVES -= 1
        if LIVES >= 0:
            print(''.join(map(str, game_word))) # makes the list a single word and prints it 
        # switch statement printing the new gameboard every turn
        match LIVES:
                case 5:
                    print(' +----+')
                    print(' |    |')
                    print(' O    |')
                    print('      |')
                    print('      |')
                    print('      |')
                    print('=======')
                case 4:
                    print(' +----+')
                    print(' |    |')
                    print(' O    |')
                    print(' |    |')
                    print('      |')
                    print('      |')
                    print('=======')
                case 3:
                    print(' +----+')
                    print(' |    |')
                    print(' O    |')
                    print('/|    |')
                    print('      |')
                    print('      |')
                    print('=======')
                case 2:
                    print(' +----+')
                    print(' |    |')
                    print(' O    |')
                    print('/|\   |')
                    print('      |')
                    print('      |')
                    print('=======')
                case 1:
                    print(' +----+')
                    print(' |    |')
                    print(' O    |')
                    print('/|\   |')
                    print('/     |')
                    print('      |')
                    print('=======')
                case 0:
                    print(' +----+')
                    print(' |    |')
                    print(' O    |')
                    print('/|\   |')
                    print('/ \   |')
                    print('      |')
                    print('=======')
                    print(f'You lose here is the word: {word}')
                    break
            
