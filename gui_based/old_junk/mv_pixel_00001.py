#
# Had to use a circle for this, pixel to small
# 0:0 starts at top left


from raylibpy import *
import math


def sin_list_build():
    # returns a list of numbers based on sine
    # 0 to 360 in incr of 10

    # a short list
    # c_list = [0, 1, 3, 4, 6, 7, 8, 9, 9, 10, 9, 9, 8, 7, 6, 4, 3, 1,0]

    angle_list = []
    for angle in range(0, 360, 10):
        y = math.sin(math.radians(angle))
        angle_list.append(int(y * 10))
        # print(int(y * 10))
    return angle_list


def main():
    screen_width: int = 800
    screen_height: int = 450
    current_x = 300
    current_y = 0
    decr_y = 10
    pause = False
    pos_x = 0

    # builds list to be used for x position
    c_list = sin_list_build()

    # initial Main window established
    init_window(screen_width, screen_height, "the moving fox?")

    shifter_y = 0       # y position movement
    shifter_curve = 0   # x position movement

    set_target_fps(40)  # I set this slow, normal is 60

    while not window_should_close():

        if is_key_pressed(KEY_P):
            if pause:
                pause = False
            else:
                pause = True

        #
        # window contents start
        begin_drawing()
        clear_background(BLACK)

        draw_text("press p to pause", 0, 0, 20, LIGHTGRAY)

        current_y = screen_height - shifter_y

        if pause is False:

            # checking to see if we are at the top of the window
            if shifter_y < screen_height:
                pos_x = current_x + c_list[shifter_curve]
                # print(str(pos_x) + " : " + str(c_list[shifter_curve]) + " : " + str(current_y))
                draw_circle(pos_x, current_y, 2, GREEN)

                # re-cycles c_list
                if shifter_curve < (len(c_list) - 1):
                    shifter_curve += 1
                else:
                    shifter_curve = 0

                # next moving up the widow on y axis
                shifter_y += 1

            else:
                draw_text(" Reached the edge of space", 0, screen_height - 20, 20, LIGHTGRAY)


        end_drawing()

    close_window()


if __name__ == '__main__':
    main()
