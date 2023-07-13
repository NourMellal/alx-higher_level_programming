#!/usr/bin/python3
""" Pascal triangle Solving ..."""


def pascal_triangle(n):
    """pascal"""
    if n <= 0:
        return []

    new_list = [[1]]
    for i in range(n - 1):
        tmp = [0] + new_list[-1] + [0]
        row = []
        for j in range(len(new_list[-1]) + 1):
            row.append(tmp[j] + tmp[j + 1])
        new_list.append(row)
    return new_list
