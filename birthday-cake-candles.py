#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    max_height = max(candles)
    return candles.count(max_height)


if __name__ == '__main__':
    candles = [4, 4, 1, 3,5,4,5,6,7,8,3,4,77,65,99,2,3]
    result = birthdayCakeCandles(candles)
    print(result)
