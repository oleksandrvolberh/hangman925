import random

word_list = ['apple', 'pear', 'mandarin', 'banana', 'mango']

word = random.choice(word_list)

guess = input('Input character (single letter) --> ')

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')

print(word_list)
print(word)
print(guess)