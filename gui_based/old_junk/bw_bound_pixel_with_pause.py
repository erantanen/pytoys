#
# Had to use a circle for this, pixel to small
# 0:0 starts at top left


from raylibpy import *


def main():
    screen_width = 800
    screen_height = 450
    current_x = 300
    current_y = 1
    shifter_y = 0
    pause = False

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
                draw_circle(current_x, current_y, 2, GREEN)
                print(current_y)
                shifter_y += 1



        end_drawing()

    close_window()


if __name__ == '__main__':
    main()
