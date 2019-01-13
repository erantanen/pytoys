#! /usr/bin/env python

'''

Silly program/toy to print a string using a vertical sin wave
as a flowing justify.

a list is built with 36 elements, 0-360 degree's

list is then built into for loop, and used as
vertically as a horizontal justification.

Update:
  april 22, 2017 -> adding cos
  
'''

import math
import time

data = '|-------|'


def sin_list_build():
    angle_list = []
    for angle in range(0, 360, 10):
        y = math.sin(math.radians(angle))
        angle_list.append(int(y * 10))
        # print(int(y * 10))
    return angle_list



def sinwave_print(wave, data, iteration):
    '''
    :param wave: a list of coords
    :param data: visual type 
    :param iteration: number of times list gets processed
    :return: 
    
    # very important printing
        https://pyformat.info/
            Parametrized formats
    '''

    a_length = len(data)
    incr = 0

    while incr < iteration:
        for i in wave:

            width = int(i) + a_length + 12
            print("{:>{width}}".format(data, width=width))
            time.sleep(.1)
        incr += 1





wave = sin_list_build()

print(wave)
print(len(wave))
b = 18
e = 36
print(wave[b:e])
sinwave_print(wave, data, 5)
