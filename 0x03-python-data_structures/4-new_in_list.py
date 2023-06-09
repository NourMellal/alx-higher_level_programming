#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return element
    tmp_list = my_list[:]
    tmp_list[idx] = element
    return tmp_list
