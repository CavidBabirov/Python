'''
Make a two-player Rock-Paper-Scissors game against computer.
Ask for player's input, compare them, print out a message to the winner.

'''

import random


mylist = ['rock', 'paper', 'scissors']

print('-----> rock')
print('-----> paper')
print('-----> scissors\n')



user = input('Birini secin ---> ').lower()
comp = random.choice(mylist)

while True:
    if user not in mylist:
        print('Yanliş seçim. Yenidən cəhd edin.')
        user = input('Birini secin ---> ').lower()

    if user == 'rock' and comp == 'scissors' or user == 'paper' and comp == 'rock' or user == 'scissors' and comp == 'paper':
        print('Tebrikler siz qazandiniz.')
        break

    elif user == comp:
        print('Beraber qaldiniz.')
        break

    else:
        print('Məğlub oldunuz.')
        break

print(f'Sizin seciminiz: {user}')
print(f'Kompyuter secimi: {comp}')

