import random

num = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')


def is_valid(n):
    if n.isdigit() and 100 >= int(n) >= 1:
        return True
    else:
        return False


while True:
    n = input()
    if is_valid(n):
        n = int(n)
        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            break
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
