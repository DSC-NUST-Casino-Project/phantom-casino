print('✯ PHANTOM CASINO ✯')

age =int(input('Hi, how old are you?:\n'))

if age < 65:
    cash = int(input('How much cash do you have on you?\n'))
    if cash >= 5000:
        print('✯ ✯ ✯ Welcome to Phantom Casino ✯ ✯ ✯\nChoose the game (number) you want to play.')

    else:
        print('You do not have enough money. Come back when you are rich')
