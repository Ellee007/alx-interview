#!/usr/bin/python3
"""
This is our python module
"""


def recursive_func(n, i, c, s):
    """
    Recursive function
    """
    if i > n:
        return 0
    elif i == n:
        return s
    elif s == n:
        return 0
    s = s + 1
    a = recursive_func(n, i, i, s)
    b = recursive_func(n, i + c, c, s)
    if min(a, b) == 0:
        return max(a, b)
    return min(a, b)


def minOperations(n):
    """
    This is our minOperation function
    """
    if n <= 1:
        return 0
    return recursive_func(n, 1, 0, 0)
