#!/usr/bin/env python3
"""
This is our python module
"""
import sys
"""
This is our sys module
"""


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
n = 0
try:
    n = int(sys.argv[1])
except Exception as e:
    print("N must be a number")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)

elems_set = {i for i in range(n)}
def recusive(elem, i, elems_set, returned_list, ignored_set):
    returned_list.append([i, elem])
    i += 1
    elems_set.remove(elem)

    j = i
    ind1 = elem
    ind2 = elem
    while j < n:
        ind1 += 1
        if ind1 < n:
            ignored_set.add([j, ind1])
        ind2 -= 1
        if ind2 >= 0:
            ignored_set.add([j, ind2])
        j += 1
    for e in elems_set:
        search_list = [i, e]
        if search_list in ignored_set:
            ignored_set.remove(search_list)
            elems_set.remove(e)
    for j in elems_set:
        if i < n:
            recusive(j, i, elems_set, returned_list, ignored_set)
