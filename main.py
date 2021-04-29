print('✯ PHANTOM CASINO ✯')

age =int(input('Hi, how old are you?:\n'))

if age > 18:
    if age < 65:
        cash = int(input('Deposit cash to be resgistered.\n (5000 Minimum) : '))
        if cash >= 5000:
            print('✯ ✯ ✯ Welcome to Phantom Casino ✯ ✯ ✯\nChoose the game (number) you want to play.\n')
            print(f'Balance : ${cash}')

            def game():
                print("Select game: \n")
                choice = int(input('1. Roulette 3000\n2. Poker 3000\n3. Blackjack 2500\n4. Craps 1500\n5. Baccarat 2000\n6. Pai Gow 1000\n7. Let Em Ride 1500 \n \n Game : '))
                if choice == 1:
                    roul = cash - 3000
                    print ('✯ You have Selected ✯')
                    print ('✯ ✯ ✯ Roulette ✯ ✯ ✯')
                    print ('✯ Enjoy the game ✯\n \n')
                    print(f'Balance : ${roul}')
                elif choice == 2:
                    poker = cash - 3000
                    print ('✯ You have Selected ✯')
                    print ('✯ ✯ ✯ Poker ✯ ✯ ✯')
                    print ('✯ Enjoy the game ✯\n \n')
                    print(f'Balance : ${poker}')
                elif choice == 3:
                    jack = cash - 2500
                    print ('✯ You have Selected ✯')
                    print ('✯ ✯ ✯ Blackjack ✯ ✯ ✯')
                    print ('✯ Enjoy the game ✯\n \n')
                    print(f'Balance : ${jack}')
                elif choice == 4:
                    craps = cash - 1500
                    print ('✯ You have Selected ✯')
                    print ('✯ ✯ ✯ Craps ✯ ✯ ✯')
                    print ('✯ Enjoy the game ✯\n \n')
                    print(f'Balance : ${craps}')
                elif choice == 5:
                    bacc = cash - 2000
                    print ('✯ You have Selected ✯')
                    print ('✯ ✯ ✯ Baccarat ✯ ✯ ✯')
                    print ('✯ Enjoy the game ✯\n \n')
                    print(f'Balance : ${bacc}')
                elif choice == 6:
                    pgow = cash - 1000
                    print ('✯ You have Selected ✯')
                    print ('✯ ✯ ✯ Pai Gow ✯ ✯ ✯')
                    print ('✯ Enjoy the game ✯\n \n')
                    print(f'Balance : ${pgow}')
                elif choice == 7:
                    lride = cash - 1500
                    print ('✯ You have Selected ✯')
                    print ('✯ ✯ ✯ Let Em Ride ✯ ✯ ✯')
                    print ('✯ Enjoy the game ✯\n \n')
                    print(f'Balance : ${lride}')
                else:
                    print('Invalid Game Input')
            game()
        else:
            print('You do not have enough money. Come back when you are rich')
    else:
        print("You have exceeded the legal age to enter Phantom Casino. We kindly urge you to seek more conservative means of redistributing the proceeds of your pension fund.")
else:
    print("You are too young to enter Phantom Casino. We will gladly accept your hard-earned money once you are of age.")
    
