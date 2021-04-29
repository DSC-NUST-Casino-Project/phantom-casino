#pyfiglet module for ASCII Art
from art import *

tprint('PHANTOM CASINO', font='random')
print('\n✯ PHANTOM CASINO ✯')

age =int(input('Hi, Enter your Age to play : '))

if age >= 18:
    if age <= 65:
        cash = int(input('\nDeposit cash to be resgistered.\n (5000 Minimum) : '))
        if cash >= 5000:
            print('\n \n✯ ✯ ✯ Welcome to Phantom Casino ✯ ✯ ✯\nChoose the game (number) you want to play.\n')
            print(f'Balance : ${cash}')
            print('\n \n✯ ✯ ✯ Get 10''%'' extra for every win on a bet ✯ ✯ ✯')

            def game():
                print("\n \nSelect game: \n")
                choice = int(input('1. Roulette 3000\n2. Poker 3000\n3. Blackjack 2500\n4. Craps 1500\n5. Baccarat 2000\n6. Pai Gow 1000\n7. Let Em Ride 1500 \n \n Game : '))
                if choice == 1:
                    roul = 3000
                    win = (roul * .1) + cash
                    loss = cash - roul
                    tprint('Roulette', font='random')
                    print ('\n✯ You have Selected ✯')
                    print ('✯ ✯ ✯ Roulette ✯ ✯ ✯')
                    print ('✯ Enjoy the game ✯\n \n')
                    print(f'Current Balance : ${loss}')

                    bet = int(input('\nPlace yout bet (1-9) : '))
                    if (bet == 1 or bet == 3 or bet == 5 or bet == 7 or bet == 9):
                        print('Congrats you have won the bet.')
                        print(f'Current balance : ${win}')
                    else:
                        print(f'You lost your ${roul}')
                        print(f'\nCurrent balance : ${loss}')

                elif choice == 2:
                    poker = 3000
                    win = (poker * .1) + cash
                    loss = cash - poker
                    tprint('Poker', font='random')

                    print ('✯ You have Selected ✯')
                    print ('✯ ✯ ✯ POKER ✯ ✯ ✯')
                    print ('✯ Enjoy the game ✯\n \n')
                    print(f'Current Balance : ${poker}')

                    bet = int(input('\nPlace yout bet (1-9) : '))
                    if (bet == 1 or bet == 3 or bet == 5 or bet == 7 or bet == 9):
                        print('Congrats you have won the bet.')
                        print(f'Balance : ${win}')
                    else:
                        print(f'You lost your ${poker}')
                        print(f'\nBalance : ${loss}')

                elif choice == 3:
                    jack = 2500
                    win = (jack * .1) + cash
                    loss = cash - jack
                    tprint('BLACKJACK', font='random')
                    print ('✯ You have Selected ✯')
                    print ('✯ ✯ ✯ Blackjack ✯ ✯ ✯')
                    print ('✯ Enjoy the game ✯\n \n')
                    print(f'Current balance : ${loss}')

                    bet = int(input('\nPlace yout bet (1-9) : '))
                    if (bet == 1 or bet == 3 or bet == 5 or bet == 7 or bet == 9):
                        print('Congrats you have won the bet.')
                        print(f'Balance : ${win}')
                    else:
                        print(f'You lost your ${jack}')
                        print(f'\nBalance : ${loss}')

                elif choice == 4:
                    craps = 1500
                    win = (craps * .1) + cash
                    loss = cash - craps
                    tprint('CRAPS', font='random')
                    print ('✯ You have Selected ✯')
                    print ('✯ ✯ ✯ Craps ✯ ✯ ✯')
                    print ('✯ Enjoy the game ✯\n \n')
                    print(f'Current balance : ${loss}')

                    bet = int(input('\nPlace yout bet (1-9) : '))
                    if (bet == 1 or bet == 3 or bet == 5 or bet == 7 or bet == 9):
                        print('Congrats you have won the bet.')
                        print(f'Balance : ${win}')
                    else:
                        print(f'You lost your ${craps}')
                        print(f'\nBalance : ${loss}')
                elif choice == 5:
                    bacc = 2000
                    win = (bacc * .1) + cash
                    loss = cash - bacc
                    tprint('BACCARAT', font='random')
                    print ('\n✯ You have Selected ✯')
                    print ('✯ ✯ ✯ Baccarat ✯ ✯ ✯')
                    print ('✯ Enjoy the game ✯\n \n')
                    print(f'Current balance : ${loss}')

                    bet = int(input('\nPlace yout bet (1-9) : '))
                    if (bet == 1 or bet == 3 or bet == 5 or bet == 7 or bet == 9):
                        print('Congrats you have won the bet.')
                        print(f'Balance : ${win}')
                    else:
                        print(f'You lost your ${bacc}')
                        print(f'\nBalance : ${loss}')
                elif choice == 6:
                    pgow = 1000
                    win = (pgow * .1) + cash
                    loss = cash - pgow
                    tprint('PAI GOW', font='random')
                    print ('\n✯ You have Selected ✯')
                    print ('✯ ✯ ✯ Pai Gow ✯ ✯ ✯')
                    print ('✯ Enjoy the game ✯\n \n')
                    print(f'Current balance : ${loss}')

                    bet = int(input('\nPlace yout bet (1-9) : '))
                    if (bet == 1 or bet == 3 or bet == 5 or bet == 7 or bet == 9):
                        print('Congrats you have won the bet.')
                        print(f'Balance : ${win}')
                    else:
                        print(f'You lost your ${pgow}')
                        print(f'\nBalance : ${loss}')

                elif choice == 7:
                    lride = 1500
                    win = (lride * .1) + cash
                    loss = cash - lride
                    tprint('LET EM RIDE', font='random')
                    print ('✯ You have Selected ✯')
                    print ('✯ ✯ ✯ Let Em Ride ✯ ✯ ✯')
                    print ('✯ Enjoy the game ✯\n \n')
                    print(f'Balance : ${lride}')

                    bet = int(input('\nPlace yout bet (1-9) : '))
                    if (bet == 1 or bet == 3 or bet == 5 or bet == 7 or bet == 9):
                        print('Congrats you have won the bet.')
                        print(f'Current balance : ${win}')
                    else:
                        print(f'You lost your ${roul}')
                        print(f'\nCurrent balance : ${loss}')

                else:
                    print('Invalid Game Input')
            game()
        else:
            print('You do not have enough money. Come back when you are rich')
    else:
        print("You have exceeded the legal age to enter Phantom Casino. We kindly urge you to seek more conservative means of redistributing the proceeds of your pension fund.")
else:
    print("You are too young to enter Phantom Casino. We will gladly accept your hard-earned money once you are of age.")
    
