import random

num = random.randint(1, 100)
print('Hi!')
print()
print('Welcome to number guessing game 🤔')
print()
name = input('What is your name, my friend? ➡️ ')
print()
print(name + ', please, enter your number below...')
print('⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️')
count = 0


def reset_data():
    global num, count
    num = random.randint(1, 100)
    count = 0


def is_play_again():
    global name
    while True:
        try_again = input(name + ', do you want to play again? (Please, enter yes or no below) ')
        if try_again == 'yes':
            return True
        elif try_again == 'no':
            return False
        else:
            print('Only yes or no answers allowed! Please put your answer again!')


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
            print('You guessed it, congratulations! 🎉')
            print()
            print('Your total number of attempts:', count)
            print()
            answer = is_play_again()
            if answer:
                reset_data()
                print('A new number has been generated. Try to guess it! 😜')
            else:
                break
    else:
        print('Please, enter an integer from 1 to 100? 🧐 ')
print()
print('👾 👾 👾 👾 👾 👾')
print(name + ', thanks for playing the number guessing game. 🌝 See you ...')
print('👾 👾 👾 👾 👾 👾')
