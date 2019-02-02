from raylibpy import *


def main():
    data = 'the quick brown fox jumped over the lazy dog'

    screen_width = 800
    screen_height= 450

    screen_width_center = int(screen_width / 3)
    screen_height_center = int(screen_height / 3)

    init_window(screen_width, screen_height, "the moving fox?")

    set_target_fps(60)

    while not window_should_close():

        begin_drawing()
        clear_background(BLACK)
        draw_text(data, screen_width_center, screen_height_center, 15, GREEN)

        end_drawing()

    close_window()


if __name__ == '__main__':
    main()
