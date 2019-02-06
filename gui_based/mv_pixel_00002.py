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
    screen_width = 800
    screen_height = 450
    middle_x = screen_width / 2
    current_y = 1
    shifter_y = 0
    pause = False

    # c_list = [0, 1, 3, 4, 6, 7, 8, 9, 9, 10, 9, 9, 8, 7, 6, 4, 3, 1, 0]
    c_list = sin_list_build()
    shifter_x = len(c_list)
    print(shifter_x)

    init_window(screen_width, screen_height, "the moving fox?")

    set_target_fps(40)

    while not window_should_close():
        clear_background(BLACK)

        if is_key_pressed(KEY_P):
            if pause:
                pause = False
            else:
                pause = True

        # checking if in pause state
        if pause is False:

            # checking if at edge of window
            if current_y == 0:
                msg_1 = 'The circle has reached the top of the screen'
                draw_text(msg_1, 20, screen_height - 20, 20, WHITE)
            else:
                current_y = screen_height - shifter_y
                current_x = int(middle_x) + c_list[shifter_x - 1]
                draw_circle(current_x, current_y, 2, GREEN)
                shifter_y += 1
                shifter_x -= 1

                if shifter_x == 0:
                    shifter_x = len(c_list)

        end_drawing()

    close_window()


if __name__ == '__main__':
    main()
