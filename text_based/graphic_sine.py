#! /usr/bin/env python

'''
a quick graphic of sine using turtle, will keep expanding this ..



'''

import math
import turtle



def sin_list_build():
    angle_list = []
    for angle in range(0, 360, 10):
        y = math.sin(math.radians(angle))
        angle_list.append(int(y * 100))
        # print(int(y * 10))
    return angle_list


wn = turtle.Screen()
wn.bgcolor('lightblue')


t = turtle.Turtle()
width =600
height = 600
# width is 600 with 0 in middle so left edge is 1/2 of
# width of window

x = width/2 * -1

turtle.setup(width, height)


t.penup()
t.setpos(x,0)
t.pendown()



y = sin_list_build()

for elm in y:
    t.goto(x, elm)
    print(x)
    x = x + 10



wn.exitonclick()
