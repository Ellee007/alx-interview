#!/usr/bin/python3
"""
This is pascal's triangle model
"""


def pascal_triangle(n):
    """
    This is pascal triangle function
    """
    p_list = []
    if (n <= 0):
        return (p_list)
    for j in range(0, n):
        for i in range(0, j + 1):
            if i == 0:
                p_list.append([])
                p_list[j].append(1)
            elif i == j:
                p_list[j].append(1)
            else:
                p_list[j].append(p_list[j - 1][i - 1] + p_list[j - 1][i])
    return (p_list)
