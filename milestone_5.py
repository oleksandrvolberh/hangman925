import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_of_guesses: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guess(self, guess):
        Checks if the letter (guess) is in the word.
    ask_for_input()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        '''
        See help(Hangman) for accurate signature
        '''
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(self.word_list)
        self.word_guessed = list('_') * len(self.word)
        
        unique_letter_dict = {}
        for letter in self.word:
            if letter not in unique_letter_dict:
                unique_letter_dict[letter] = 1
            else:
                unique_letter_dict[letter] += 1
        self.num_letters = len(unique_letter_dict.keys())

        self.list_of_guesses = []

        print(f'The mistery word has {self.num_letters} UNIQUE characters')
        

    def check_guess(self, guess):
        '''
        Checks if the letter(guess) is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        guess: str
            The letter to be checked
        '''
        if guess in self.word:
            print(f'Good guess! \'{guess}\' is in the word.')
            for index, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[index] = guess
                else:
                    pass
            self.num_letters -= 1 
        else:
            self.num_lives -= 1
            print(f'Sorry, \'{guess}\' is not in the word. Try again.')  
            print(f'You have {self.num_lives} lives left.')  

    def ask_for_input(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        while True:
            print(f'The computer thought of a word {self.word_guessed}')
            print(f'Letters that you have already called {self.list_of_guesses}')
            guess = input('Guess the letter --> ').lower()
            if not (len(guess) == 1 and guess.isalpha()):
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif (guess in self.list_of_guesses):
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
         
def play_game(word_list):
    
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print(f'You lost! The word was \'{game.word}\'')
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives != 0 and game.num_letters == 0:
            print(f'The computer thought of a word {game.word_guessed}')
            print('Congratulations. You won the game!')
            break

if __name__ == '__main__':
    word_list = ['apple', 'pear', 'mandarin', 'banana', 'mango']
    play_game(word_list) 