#!/usr/bin/python3
def max_integer(my_list=[]):
    num_max = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > num_max:
            num_max = my_list[i]
    return num_max
    