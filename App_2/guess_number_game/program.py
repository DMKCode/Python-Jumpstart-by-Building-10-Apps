import random

print('-----------------------------------')
print('     GUESS THAT NUMBER GAME')
print('-----------------------------------')
print()

name = input('What is your name? ')
guess = -1

the_number = random.randint(0, 100)
while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Sorry {1}, your guess of {0} is too LOW'.format(name, guess))
    elif guess > the_number:
        print('Sorry {1}, your guess of {0} is too HIGH'.format(name, guess))
    else:
        print('Excellent work {0}, you won, it was {1}'.format(name, guess))

print('done')