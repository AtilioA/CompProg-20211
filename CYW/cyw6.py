#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'decode_message' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING encrypted_input as parameter.
#

def decode_message(encrypted_input):
    string, n = encrypted_input.split(' / ')
    n = int(n)

    if n == 1:
        return string

    rows = ["" for char in range(len(string))]

    row = 0
    for i in range(len(string)):
        rows[row] = rows[row] + string[i]

        if row == n - 1:
            down = False
        elif row == 0:
            down = True

        if down:
            row = row + 1
        else:
            row = row - 1

    encoded = ''.join(rows)
    return encoded


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    encrypted_input = input()

    result = decode_message(encrypted_input)

    fptr.write(result + '\n')

    fptr.close()
