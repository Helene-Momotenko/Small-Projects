import random

num = random.randint(1, 100)
print('Welcome to number guessing game 🤔')
count = 0


def is_valid(n):
    if n.isdigit() and 100 >= int(n) >= 1:
        return True
    else:
        return False


while True:
    n = input()
    if is_valid(n):
        n = int(n)
        count += 1
        if n < num:
            print('Your number is less 😔 than expected, please try again 😿')
        elif n > num:
            print('Your number is higher 😮 than expected, please try again 😿')
        else:
            print('You guessed it, congratulations!🎉')
            break
    else:
        print('Please, enter an integer from 1 to 100? 🧐 ')
print('Your total number of attempts:', count)
print('Thanks for playing the number guessing game. 🌝 See you ...')
