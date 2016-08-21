#-------------------------------------------------------------------------

#                   Lab1TJ.py

#-------------------------------------------------------------------------

#                Teagan Johner

#                  Program name:  Right Aligned Lists
#-------------------------------------------------------------------------

import random

def gen_word():
    length = random.randint( 3, 15 )
    valid_letters='abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(valid_letters) for i in range(length))    

def gen_list():
    y = []
    x = random.randint( 5, 12 )
    for i in range(x):
        z = gen_word
        y.append(z)
    print(y)


# def max_length(listOfStrings):
    



# def print_right_aligned():