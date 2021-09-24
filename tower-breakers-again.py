#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def towerBreakers(arr):
    # Write your code here

    arr.sort(reverse=True)
    # print(arr)
    cur_player = 1

    for idx, twr in enumerate(arr):
        # print(twr)
        if twr > 1 and idx < (len(arr) - 1):  # move on to the next player
            cur_player += 1
        elif twr > 1 and idx == (len(arr) -1):  # can break down the tower and is the last turn
            break
        elif twr == 1:
            cur_player -= 1
            break

    winner = 1 if cur_player % 2 == 1 else 2
    return winner


if __name__ == '__main__':

    os.environ['OUTPUT_PATH'] = '../tower-breakers-again-output.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Number of Test Cases and number of time will loop

    for t_itr in range(t):  # Loop number of times per test case

        arr_count = int(input().strip())  # Number of Towers

        arr = list(map(int, input().rstrip().split()))  # Height of each of the towers

        result = towerBreakers(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
