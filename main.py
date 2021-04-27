print('✯ PHANTOM CASINO ✯')

age =int(input('Hi, how old are you?:\n'))

if age > 18:
    if age < 65:
        cash = int(input('How much cash do you have on you?\n'))
        if cash >= 5000:
            print('✯ ✯ ✯ Welcome to Phantom Casino ✯ ✯ ✯\nChoose the game (number) you want to play.')

        else:
            print('You do not have enough money. Come back when you are rich')
    else:
        print("You have exceeded the legal age to enter Phantom Casino. We kindly urge you to seek more conservative means of redistributing the proceeds of your pension fund.")
else:
    print("You are too young to enter Phantom Casino. We will gladly accept your hard-earned money once you are of age.")
    
