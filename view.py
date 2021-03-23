# This was creating by me, Giovanni Neves Sadauscas.
# There is m github: https://github.com/gionneves

import os

class View:

###
#the 'show_msg' function is use to print a message between '#'
#
#@param msg
#gives the function what message will display between the '#'
###
    def show_msg(self, msg):
        print('#'*(round(len(msg)/2)*5))
        print(' '*round(len(msg)/2) + msg)
        print('#'*(round(len(msg)/2)*5))
        pass

###
# the 'spaceLine' function is use to jump a line, in the middle will put a bar of
# '#' when display
###
    def spaceLine(self):
        print()
        print('#'*15)
        print()
        pass

###
# the 'clear' function is auto explaining. He clear the console for the new information
###
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        pass

###
# The 'choices' function display the choices when the params is definy
#
# @param a, b, c, d
# They has the same objective to show the text inside him but display in order, like
# a = 1, b = 2, c = 3, d = 4.
#
# If one of this param has a string 'null' they will not display
###
    def choices(self, a, b, c, d):
        if a != 'null':
            print('1 - ' + a)
        else:
            pass
        if b != 'null':
            print('2 - ' + b)
        else:
            pass
        if c != 'null':
            print('3 - ' + c)
        else:
            pass
        if d != 'null':
            print('4 - ' + d)
        else:
            pass
        pass

# ------------------------- game is on ------------------------

    def odd_msg(self, number_divides):
        print('My number is ODD, try think something close ' + str(number_divides))
        pass

    def odd_number(self):
        print('My number is ODD')
        pass

    def pair_msg(self, number_divides):
        print('My number is PAIR, try think something close ' + str(number_divides))
        pass

    def pair_number(self):
        print('My number is PAIR')
        pass
