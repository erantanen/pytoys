
from raylibpy import *


def main():

    data = 'the quick brown fox jumped over the lazy dog'

    screen_width: int = 800
    screen_height: int = 450

    screen_width_center = int(screen_width/3)
    screen_height_center = int(screen_height/3)

    init_window(screen_width, screen_height, "the moving fox?")

    shifter = 0

    set_target_fps(60)

    while not window_should_close():
        clear_background(BLACK)
        draw_text(data, screen_width_center+shifter, screen_height_center-shifter, 15, GREEN)
        shifter += 1
        end_drawing()

    close_window()


if __name__ == '__main__':
    main()
