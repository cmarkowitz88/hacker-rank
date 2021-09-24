# !/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):

    size = len(arr)
    print(size)
    left_to_right_sum = 0
    right_to_left_sum = 0

    for i, lst in enumerate(arr):
        # Get the values for both left-right and right-left diagonals in the same pass
        left_to_right_sum += lst[i]
        right_to_left_sum += lst[len(lst)-(i+1)]

    return abs(left_to_right_sum - right_to_left_sum)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input().strip())

    arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]

    # for _ in range(n):
    # arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
