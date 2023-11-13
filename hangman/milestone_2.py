import random

word_list = ['banana', 'apple', 'orange', 'strawberry', 'watermelon']
print(random.choice(word_list))

word = input('Enter a single letter:')
print(word)

'''############## Choosing a single letter at random ####################'''

guess = input('Enter a single letter:')

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")

else: print("Oops! That is not a valid input")
