#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    comp = my_list[0]
    for i in range(len(my_list)):
        if comp < my_list[i]:
            comp = my_list[i]
    return comp
