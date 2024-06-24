!/usr/bin/python3
"""
This is our python module
"""


def validUTF8(data):
    """
    This is a function that checks if data is a valid utf8 incoding
    """
    continuation = 0
    for d in data:
        binary_d = bin(d)[2:]
        length = len(binary_d)
        if length > 8:
            binary_d = binary_d[length - 8:]
            d = int(binary_d, 2)
        elif length < 8:
            for i in range(8 - length):
                binary_d = "0" + binary_d
        if continuation == 0:
            if binary_d[0] == "0":
                continue
            if binary_d[1:3] == "10":
                continuation = 1
            elif binary_d[1:4] == "110":
                continuation = 2
            elif binary_d[1:5] == "1110":
                continuation = 3
            elif binary_d[1:6] == "11110":
                continuation = 4
            elif binary_d[1:7] == "111110":
                continuation = 5
            else:
                return False
            continue
        if binary_d[0:2] == "10":
            continuation = continuation - 1
        else:
            return False
    if continuation != 0:
        return False
    return True
