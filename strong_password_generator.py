import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

not_clear_symbols = 'il1Lo0O'

chars = ''


def check_answer_integer_and_valid(question):
    while True:
        answer = input(question)
        if answer.isdigit() and int(answer) >= 1:
            return int(answer)
        else:
            print('Only positive integers values required!')


def confirm_message(question):
    while True:
        answer = input(question)
        if 'yes' == answer.lower():
            return True
        elif 'no' == answer.lower():
            return False
        else:
            print('Only reply yes/no required!')


def filter_chars(chars, not_clear_symbols):
    new_chars = ''
    for letter in chars:
        if letter not in not_clear_symbols:
            new_chars += letter
    return new_chars


quantity_passwords = check_answer_integer_and_valid('Please, enter how many passwords need to be generated: ')

for i in range(quantity_passwords):
    password_length = check_answer_integer_and_valid('Enter the number of symbols required:')
    is_digits_needed = confirm_message('Any digits in password?')
    is_uppercase_letters_needed = confirm_message('Any uppercase letters in password?')
    is_lowercase_letters_needed = confirm_message('Any lowercase letters in password?')
    is_punctuation_needed = confirm_message('Any punctuation in password?')
    is_unclear_symbols_needed = confirm_message('Any unclear symbols needed?')

    if is_digits_needed:
        chars += digits
    if is_uppercase_letters_needed:
        chars += uppercase_letters
    if is_lowercase_letters_needed:
        chars += lowercase_letters
    if is_punctuation_needed:
        chars += punctuation
    if not is_unclear_symbols_needed:
        chars = filter_chars(chars, not_clear_symbols)
    print(*random.sample(chars, password_length), sep='')

    chars = ''

print('Thank you')
