#
# Had to use a circle for this, pixel to small
# 0:0 starts at top left


from raylibpy import *


def main():
    screen_width: int = 800
    screen_height: int = 450
    current_x = 300
    current_y = 0
    decr_y = 10
    pause = False
    pos_x = 0

    c_list = [0, 1, 3, 4, 6, 7, 8, 9, 9, 10, 9, 9, 8, 7, 6, 4, 3, 1, 0]

    init_window(screen_width, screen_height, "the moving fox?")

    shifter_y = 0
    shifter_curve = 0

    set_target_fps(40)

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
            # shifts position of x by c_list increment

            if shifter_y < screen_height:
                pos_x = current_x + c_list[shifter_curve]
                print(str(pos_x) + " : " + str(c_list[shifter_curve]) + " : " + str(current_y))
                draw_circle(pos_x, current_y, 2, GREEN)

                if shifter_curve < (len(c_list) - 1):
                    shifter_curve += 1
                else:
                    shifter_curve = 0

                shifter_y += 1

            else:
                draw_text(" Reached the edge of space", 0, screen_height-20, 20, LIGHTGRAY)



        end_drawing()

    close_window()


if __name__ == '__main__':
    main()
