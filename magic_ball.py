import random

answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely",
           "You may rely on it", "As I see it, yes", "Most likely", "Outlook good",
           "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
           "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
           "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good",
           "Very doubtful"]
print('✨    ✨     ✨     ✨     ✨')
print('Hello World!')
print()
print('I am a magic ball 🎱 and I know the answer to any question you may have.')
print('✨    ✨     ✨     ✨     ✨')
name = input('First of all, tell me your name, please.  ➡️  ')
print()
print('👋 Hello,' + name + '!')
print()


def is_play_again():
    global name
    while True:
        try_again = input(name + ', do you want to ask again? (Please, enter yes or no below) ').lower()
        if try_again == 'yes':
            return True
        elif try_again == 'no':
            return False
        else:
            print('Only yes or no answers allowed! Please put your answer again!')


while True:
    question = input(name + ', ask me everything you want!')
    print(random.choice(answers))
    if not is_play_again():
        print('👀 Come back when you got a question! 👀')
        print('✨    ✨     ✨     ✨     ✨')
        break
