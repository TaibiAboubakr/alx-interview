#!/usr/bin/python3
""" pascal triangle """


def pascal_triangle(n):
    """ pascal function """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prev_list = triangle[-1]
        new_list = [1]
        for j in range(1, i):
            new_list.append(prev_list[j - 1] + prev_list[j])
        new_list.append(1)
        triangle.append(new_list)
    return triangle
