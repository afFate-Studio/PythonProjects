from random import randint
import pyinputplus as pyip

def update_game_word(word, game_word, user_guess):
    game_word = list(game_word)
    for index, letter in enumerate(word):
        if user_guess == letter:
            game_word[index] = user_guess
    return ''.join(game_word)

def check_guessed(user_guesses, user_guess):
    return user_guess in user_guesses

def print_gameboard(LIVES, game_word, word):
    match LIVES:
            case 6:
                print(' +----+')
                print(' |    |')
                print('      |')
                print('      |')
                print('      |')
                print('      |')
                print('=======')
                print(f"you have {LIVES} lives remaining")
                print(game_word)
            case 5:
                print(' +----+')
                print(' |    |')
                print(' O    |')
                print('      |')
                print('      |')
                print('      |')
                print('=======')
                print(f"you have {LIVES} lives remaining")
                print(game_word)
            case 4:
                print(' +----+')
                print(' |    |')
                print(' O    |')
                print(' |    |')
                print('      |')
                print('      |')
                print('=======')
                print(f"you have {LIVES} lives remaining")
                print(game_word)
            case 3:
                print(' +----+')
                print(' |    |')
                print(' O    |')
                print('/|    |')
                print('      |')
                print('      |')
                print('=======')
                print(f"you have {LIVES} lives remaining")
                print(game_word)
            case 2:
                print(' +----+')
                print(' |    |')
                print(' O    |')
                print('/|\   |')
                print('      |')
                print('      |')
                print('=======')
                print(f"you have {LIVES} lives remaining")
                print(game_word)
            case 1:
                print(' +----+')
                print(' |    |')
                print(' O    |')
                print('/|\   |')
                print('/     |')
                print('      |')
                print('=======')
                print(f"you have {LIVES} lives remaining")
                print(game_word)
            case 0:
                print(' +----+')
                print(' |    |')
                print(' O    |')
                print('/|\   |')
                print('/ \   |')
                print('      |')
                print('=======')
                print(f"you have {LIVES} livesremaining")
                print(f'You lose here is the word: {word}')
            
def main():
    #######################################################################################################################################
    # Variables                                                                                                                           #
    # word list for the game                                                                                                              #
    word_list = ["aardvark", "baboon", "camel"]                                                                                           #
    word = word_list[randint(0, len(word_list)-1)] # dynamic randint based on the word_list used to choose a word from the list           #
    game_word = []      # empty list used to keep track of if the user guessed the correct value                                          #
    user_guesses = [] # empty list to keep track of user guesses                                                                          #
    LIVES = 6                                                                                                                             #
    #######################################################################################################################################
    """
        iterates over the length of the chosen word and then appends the correct amount
        of '_' to game_word list
    """
    for i in range(len(word)):
        game_word.append('_') # appends to a list, used to keep track of if the user guessed the correct value
    print(''.join(map(str, game_word)))  # shows user the length of the word without showing the word

    while True:
        
        if LIVES == 0:
            break

        user_guess = pyip.inputStr("Guess a letter: ")[0].lower() # splices user string to first character then makes it lowercase

        """
            checks user guess and then replaces the '_' in game_word with the letter
            if the guess was correct.
        """
        
        if len(user_guesses) != 0:
            while True:
                guessed = check_guessed(user_guesses, user_guess)
                if not guessed:
                    break
                else:
                    user_guess = pyip.inputStr("Guess a letter: ")[0].lower()
        
        user_guesses.append(user_guess)
        game_word = update_game_word(word, game_word, user_guess)
        
        if LIVES != 0:
            if game_word == word:
                print('You win!')
                break
            elif user_guess in word:
                print_gameboard(LIVES, game_word, word)
            else:
                LIVES -= 1
                print_gameboard(LIVES, game_word, word)

if __name__ == '__main__':
    main()