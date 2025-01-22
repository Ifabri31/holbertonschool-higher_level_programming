#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    my_list = set(my_list)
    my_list = list(my_list)
    for element in my_list:
        result += element
    return (result)
