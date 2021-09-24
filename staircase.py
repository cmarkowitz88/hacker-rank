#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    space = " "
    val = "#"
    count = 1

    while n > 0:
        print(space * (n - 1), end="")
        print(val * count)
        n = n - 1
        count = count + 1


if __name__ == '__main__':
    # n = int(input().strip())
    n = 5
    staircase(n)
