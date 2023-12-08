import random

word_list = ['apple', 'pear', 'mandarin', 'banana', 'mango']
word = random.choice(word_list)

print(word_list)
print(word)

def check_guess(guess):
    if word.find(guess) >= 0:
        print(f'Good guess! \'{guess}\' is in the word.')
    else:
        print(f'Sorry, \'{guess}\' is not in the word. Try again.')    

def ask_for_input():
    while True:
        guess = input('Guess the letter --> ').lower()
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    
    check_guess(guess)

ask_for_input()

# print(guess)