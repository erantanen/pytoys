import math


#
# output
# [0, 1, 3, 4, 6, 7, 8, 9, 9, 10, 9, 9, 8, 7, 6, 4, 3, 1, 0
#   , -1, -3, -5, -6, -7, -8, -9, -9, -10, -9, -9, -8, -7, -6, -5, -3, -1]

def sin_list_build():
    angle_list = []
    for angle in range(0, 360, 10):
        y = math.sin(math.radians(angle))
        apl = 30
        angle_list.append(int(y * apl))
        # print(int(y * 10))
    return angle_list






def main():
    wave = sin_list_build()

    a_list = [0, 1, 3, 4, 6, 7, 8, 9, 9, 10, 9, 9, 8, 7, 6, 4, 3, 1]
    a_len = len(a_list)
    b_list = []
    c_list = a_list
    r_cycle = 0

    #for elm in a_list:
    while r_cycle < 17:

        if len(b_list) < 9:
            b_list.append(a_list[r_cycle])
        else:
            b_list.pop(0)
            b_list.append(a_list[r_cycle])

        print("-------\n")
        print(b_list)
        print(len(b_list))
        print(a_list)
        r_cycle += 1



if __name__ == '__main__':
    main()
