
from nltk.corpus import wordnet

#words = [x.name().split(".")[0] for x in wordnet.all_synsets('n')]

# with open('file.txt', 'w') as f:
#     for item in words:
#         f.write("%s\n" % item)

list_of_words = []

f = open('file.txt', 'r')
for word in f:
    word = word.strip()
    if len(wordnet.synsets(word)) >= 3:
        list_of_words.append((word, wordnet.synsets(word)[0].definition(),wordnet.synsets(word)[1].definition(),wordnet.synsets(word)[2].definition()))

from random import choice

print('Welcome to "Guess the Word Game!"')

while 1 == 1:

    print('You have 3 attempts at guessing the word')
    print("Let's begin!")
    print('\n')

    word_to_guess = choice(list_of_words)
    count = 0
    limit = 3
    correct_answer = 0

    while count < limit:

        print('The definition is:\n', word_to_guess[count+1])
        word = input('Answer: ')
        count += 1

        if word.lower() == word_to_guess[0]:
            print('Huray! :)')
            correct_answer = 1
            break

        else:
        # if letter_guess not in word:
            print('Wrong! Guess again! Here’s another hint: ')

    if count < limit or correct_answer == 1:
        print('Congrats!')
    else:
        print('Unlucky! The answer was,', word_to_guess[0])

    print('\n')
    user_answer = input('Leave the game Y/N: ')

    if user_answer.upper() == 'Y':
        break