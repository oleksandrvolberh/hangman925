import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        
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


    def check_guess(self, guess):

        self.guess = guess.lower()
        if self.guess in self.word:
            print(f'Good guess! \'{self.guess}\' is in the word.')
            for index, letter in enumerate(self.word):
                if letter == self.guess:
                    self.word_guessed[index] = letter
                else:
                    pass
            self.num_letters -= 1 
        else:
            self.num_lives -= 1
            print(f'Sorry, \'{guess}\' is not in the word. Try again.')  
            print(f'You have {self.num_lives} lives left.')  


    def ask_for_input(self):

        while True:
            guess = input('Guess the letter --> ')
            if not (len(guess) == 1 and guess.isalpha()):
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif (guess in self.list_of_guesses):
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

                print(self.list_of_guesses)
                print(self.word_guessed)


word_list = ['apple', 'pear', 'mandarin', 'banana', 'mango']
hungman = Hangman(word_list, 5)

print(word_list)
print(hungman.word)

hungman.ask_for_input()

                