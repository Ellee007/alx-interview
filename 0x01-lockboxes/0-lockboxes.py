#!/usr/bin/python3
"""
This is our lockbox model
"""


def canUnlockAll(boxes):
    """
    Lockbox function
    """
    n = len(boxes)
    unlocked = [0]
    a = 1
    i = 0
    while i < a:
        for elem in boxes[unlocked[i]]:
            if elem < n and elem not in unlocked:
                unlocked.append(elem)
                a += 1
        i += 1
        if a == n:
            return True
    return False
