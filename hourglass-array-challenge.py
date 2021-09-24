# HackerRank URL: https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(in_arr):

    row_count = 0
    col_count = 0
    arr_result = []
    tmp_totl = 0

    for row in in_arr:
        col_count = 0

        for col in row:
            if row_count <= 3:
                if col_count <= 3:
                    tmp_totl = in_arr[row_count][col_count] + in_arr[row_count][col_count+1] + in_arr[row_count][col_count+2]
                    tmp_totl += in_arr[row_count+1][col_count+1]
                    tmp_totl += in_arr[row_count+2][col_count] + in_arr[row_count+2][col_count+1] + in_arr[row_count+2][col_count+2]
                    arr_result.append(tmp_totl)
                else:
                    break
            else:
                break

            col_count += 1
        row_count += 1

    return max(arr_result)


if __name__ == '__main__':
    arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]

    result = hourglassSum(arr)

    print(str(result) + '\n')
