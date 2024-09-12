#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_true_false = []
    for num in my_list:
        if num % 2 == 0:
            list_true_false.append(True)
        else:
            list_true_false.append(False)
    return list_true_false
