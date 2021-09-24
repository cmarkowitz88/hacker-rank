#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):

    pos = 0.0
    neg = 0.0
    zero = 0.0

    for x in arr:
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        else:
            zero += 1

    print("{0:.5f}".format(pos / len(arr)))
    print("{0:.5f}".format(neg / len(arr)))
    print("{0:.5f}".format(zero / len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)