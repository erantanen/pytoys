
import math
import time

from raylibpy import *


def sin_list_build():
    '''
    output:
        [0, 1, 3, 4, 6, 7, 8, 9, 9, 10, 9, 9, 8, 7, 6, 4, 3, 1, 0,
         -1, -3, -5, -6, -7, -8, -9, -9, -10, -9, -9, -8, -7, -6, -5, -3, -1]
    :return:
    '''

    angle_list = []
    for angle in range(0, 360, 10):
        y = math.sin(math.radians(angle))
        # changing apl adds to peak
        apl = 30
        angle_list.append(int(y * apl))
        # print(int(y * 10))
    return angle_list


def list_rotate(wave, r_cycle, b_list):

    a_list = wave


    if len(b_list) < 9:
        b_list.append(a_list[r_cycle])
    else:
        b_list.pop(0)
        b_list.append(a_list[r_cycle])

    return b_list


def main():

    data = 'the quick brown fox jumped over the lazy dog'
    wave = sin_list_build()

    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "the moving fox?")


    set_target_fps(60)

    x_pos = 200
    y_pos = 30
    y_shift = 0
    r_cycle = 0
    b_list = []

    while not window_should_close():

        # starts everything off
        begin_drawing()

        # cleans window
        clear_background(BLACK)

        draw_rectangle(10, 0, screen_width-20, 25, WHITE)

        b_list = list_rotate(wave, r_cycle, b_list)

        for x_shift in b_list:
            draw_text(data, x_pos+x_shift, y_pos+y_shift, 15, GREEN)
            r_cycle += 1
            y_shift += 10


        end_drawing()

    close_window()


if __name__ == '__main__':
    main()
