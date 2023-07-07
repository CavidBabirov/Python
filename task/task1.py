'''
Generate a random number between 1 and 100. Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

'''

import random

number = random.randint(0, 100)
number_list = []

while True:
    user = int(input('Bir reqem daxil edin --->  '))

    # if not type(user) is int:
    #     raise TypeError('Yalniz reqem daxil edin!\n')

    number_list.append(user)

    if user < 0 or user > 100:
        raise Exception('0 ile 100 arasinda bir reqem daxil edin!\n')
        
            
    if user == number:
        print(f'\nTebrikler dogru texmin etdiniz. {number}')
        print(f'Daxil etdiyiniz reqemler: {number_list} ')
        print(f'Cəhdlərinizin sayi: {len(number_list)} \n')
        break

    elif user > number:
        print('Asagi reqem daxil edin.\n')

    elif user < number:
        print('Yuxari reqem daxil edin.\n')
        