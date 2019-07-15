#
# Had to use a circle for this, pixel to small
# 0:0 starts at top left


from raylibpy import *
import math


def fib_dic_list(num):

    fib_list = [1,1, 2, 3, 5, 8, 13, 21, 34]
    size_dict ={}

    for elm_layer in range(1, num):
        size_dict[elm_layer] = fib_list[:elm_layer]

    return size_dict







def main():
    screen_width = 800
    screen_height = 450
    middle_x = screen_width / 2
    current_y = 1
    shifter_y = 0
    pause = False
    num_boxes = 9
    builder_incr = 1

    init_window(screen_width, screen_height, "the moving fox?")

    set_target_fps(30)

    rec_sizing = fib_dic_list(num_boxes)




    while not window_should_close():
        clear_background(BLACK)

        begin_drawing()

        if builder_incr > (num_boxes-1):
            builder_incr = 1
        else:
            build_layer = rec_sizing[builder_incr]
            print(build_layer)


            for rec_size in build_layer:
                draw_rectangle_lines(int(screen_width/2), int(screen_height/2), rec_size*8, rec_size*8, WHITE)
            builder_incr += 1


        end_drawing()


    close_window()


if __name__ == '__main__':
    main()
