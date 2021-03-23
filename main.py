import visual.view
import os
import random

ver = visual.view.View()

# ---------------------- generator -------------------------

def generator():
    return random.randint(1, 30)
    pass

# ---------------------- Logic -------------------------

def gameStart():
    ver.clear()
    game = True
    tipEnable = 1
    number = generator()

    def tipToss(tip):
        if tip > 0:
            if tip == 3:
                if (number % 2) == 0:
                    if (number - 4) > 0:
                        ver.pair_msg(number - 4)
                    else:
                        ver.pair_number()
                else:
                    if (number + 4) < 30:
                        ver.odd_msg(number + 4)
                    else:
                        ver.odd_number()
                        pass

            elif tip == 2:
                if (number - 7) < 0:
                    x = 0
                else:
                    x = number - 7
                    pass

                if (number + 7) > 30:
                    y = 30
                else:
                    y = (number + 7)
                    pass


                print('The number is between {} and {}'.format(x, y))

            elif tip == 1:
                for x in range(30):
                    for y in range(10):
                        multi = x * y
                        print(multi)
                        if multi == number:
                            print('The number is a multiple of ' + str(y))
                            break
            else:
                print('The number is a prime number')

        else:
            print("There is no more tips")
            pass
        pass


###
# The 'choice_game' funcition is use to send the player to what he choices
#
# @param c
# The param 'c' is use to get the choice of player and what he want to do
###
    def choice_game(c):
        if c == 1:
            gameStart()
        elif c == 2:
            tipToss(tipEnable)
        elif c == 3:
            goCredits()
        else:
            os.system('exit')
        pass

    ver.show_msg('Game Start!')
    print('Try guess the number between 0 and 30 the computer pick up')

    while game:
        ver.spaceLine()
        ver.choices('Guess a number', 'Get a tip', 'null', 'null')
        inp = int(input('Select your choice: '))
        choice_game(inp)
        pass
    pass

###
# The 'choice_menu' funcition is use to send the player to what he choices
#
# @param c
# The param 'c' is use to get the choice of player and identify where he wanna go
###
def choice_menu(c):
    if c == 1:
        gameStart()
    elif c == 2:
        gameStartDebug()
    elif c == 3:
        goCredits()
    else:
        os.system('exit')
    pass


# ----------------------- Visual ------------------------

ver.clear()
ver.show_msg('Wellcome to Guessing game')
ver.choices('Start game', 'Start debug game', 'Credits', 'Exit')

inp = int(input('Enter your choice: '))
choice_menu(inp)
