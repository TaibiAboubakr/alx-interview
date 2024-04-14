#!/usr/bin/python3
""" pascal triangle """


def pascal_triangle(n):
    """ pascal function """
    if n <= 0:
        return []
    elif n == 1:
        return ([[1]])
    elif n == 2:
        return ([[1], [1, 1]])
    triangle = [[1], [1, 1]]
    for i in range(3, n + 1):
        prv_list = triangle[i-2]
        list = [1]
        lenght = len(prv_list)
        for j in range(lenght - 1):
            list.append(prv_list[j] + prv_list[j+1])
        list.append(1)
        triangle.append(list)
    return (triangle)
