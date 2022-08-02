import random

word_list = ['milk', 'movie', 'mother', 'wall', 'garden', 'language', 'teacher', 'student', 'computer',
             'capitalism', 'optimist', 'government', 'happiness', 'station', 'spaceship']


def get_word():
    word = random.choice(word_list).upper()
    return word


def get_guessed_word_or_letter():
    while True:
        guessed_word = input('Please, enter a letter or a full word: ')
        if guessed_word.isalpha():
            break
        else:
            print(f'Error: {guessed_word} is NOT a letter or a full word!')
    return guessed_word.upper()


def display_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def play(word):
    word_completion = list('_' * len(word))
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play in Hangman!")

    while True:
        print()
        print(display_hangman(tries))
        print(*word_completion)
        guessed_word_or_letter = get_guessed_word_or_letter()
        if guessed_word_or_letter in guessed_words or guessed_word_or_letter in guessed_letters:
            print('This word or letter has already been mentioned. Guess again :) ')
        else:
            if len(guessed_word_or_letter) == 1:
                guessed_letters.append(guessed_word_or_letter)
                if guessed_word_or_letter in word:
                    print(f'Oh, you are right! The letter {guessed_word_or_letter} is in the word!')
                    for letter_index in range(len(word)):
                        if word[letter_index] == guessed_word_or_letter:
                            word_completion[letter_index] = guessed_word_or_letter
                    if '_' not in word_completion:
                        print('You won!')
                        break
                else:
                    print(f'The letter {guessed_word_or_letter} is NOT in guessed word! Try again!')
                    tries -= 1
            else:
                guessed_words.append(guessed_word_or_letter)

                if guessed_word_or_letter == word:
                    print('You won!')
                    break
                else:
                    print(f'The word {guessed_word_or_letter} is not correct. Try again.')
                    tries -= 1


play(get_word())
