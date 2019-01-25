#
# Had to use a circle for this, pixel to small
# 0:0 starts at top left


from raylibpy import *


def main():
    screen_width: int = 800
    screen_height: int = 450
    current_x = 300
    current_y = 0
    decr_y  = 10

    c_list = [0, 1, 3, 3, 4, 6, 6, 7, 8, 8, 9, 9, 10]

    init_window(screen_width, screen_height, "the moving fox?")

    shifter_y = 0
    shifter_curve = 0

    set_target_fps(40)

    while not window_should_close():
        clear_background(BLACK)

        current_y = screen_height - shifter_y

        draw_circle(current_x + c_list[shifter_curve], current_y, 2, GREEN)

        shifter_y += 1

        end_drawing()

    close_window()


if __name__ == '__main__':
    main()
