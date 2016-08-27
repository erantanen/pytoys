'''
Silly program/toy to print a string using a vertical sin wave
as a flowing justify.

a list is built with 36 elements, 0-360 degree's

list is then built into for loop, and used as
vertically as a horizontal justification.


'''

import math
import time

data = 'the brown fox jumped over the lazy dog'


def sin_list_build():
    angle_list = []
    for angle in range(0, 360, 10):
        y = math.sin(math.radians(angle))
        angle_list.append(int(y * 10))
        # print(int(y * 10))
    return angle_list


def sinwave_print(wave, data, iteration):
    a_length = len(data)
    incr = 0
    while incr < iteration:
        for i in wave:
            width = int(i) + a_length + 12
            print("{:>{width}}".format(data, width=width))
            time.sleep(.1)
        incr += 1





wave = sin_list_build()
sinwave_print(wave, data, 5)
