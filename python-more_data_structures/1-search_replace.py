#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_2 = []
    for i in my_list:
        if i == search:
            list_2.append(replace)
        else:
            list_2.append(i)
    return list_2
