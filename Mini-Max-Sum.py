#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    min = arr[0] + arr[1] + arr[2] + arr[3]
    max = arr[1] + arr[2] + arr[3] + arr[4]
    print(str(min) + ' ' + str(max))


if __name__ == '__main__':
    # arr = list(map(int, input().rstrip().split()))
    arr = [5, 4, 3, 2, 1]

    miniMaxSum(arr)
