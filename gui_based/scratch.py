import math
import time


""" 
A rework to prep for a gui, but also uses a dictionary
instead of a straight list. 

Jan 16, 2019


"""

def sin_list_build():
    angle_list = []
    for angle in range(0, 360, 10):
        y = math.sin(math.radians(angle))
        angle_list.append(int(y * 10))
        # print(int(y * 10))
    return angle_list


def it_dict(c_list):
    # {0: 0, 1: 1, 2: 3, 3: 4, 4: 6, 5: 7, 6: 8, 7: 9, 8: 9,
    #      9: 10, 10: 9, 11: 9, 12: 8, 13: 7, 14: 6, 15: 4, 16: 3, 17: 1}
    # c_list = [0, 1, 3, 4, 6, 7, 8, 9, 9, 10, 9, 9, 8, 7, 6, 4, 3, 1]

    dict_sine = dict(enumerate(c_list))
    return dict_sine


def main():
    triger = 0
    end = 100
    outer_break = 0

    data = 'the brown fox jumped over the lazy dog'
    a_length = len(data)

    off_sets = it_dict(sin_list_build())
    offset_len = len(off_sets)

    while triger < end:

        if outer_break == 5:
            break

        if triger < offset_len:
            width = off_sets[triger] + a_length + 12
            print("{:>{width}}".format(data, width=width))
            triger += 1
            time.sleep(.1)
        else:
            triger = 0
            outer_break += 1


if __name__ == '__main__':
    main()
