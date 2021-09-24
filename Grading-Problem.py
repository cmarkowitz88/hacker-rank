#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(in_grades):
    # Write your code here
    rounded_grades = []

    del(in_grades[0])

    for g in in_grades:
        remainder = g % 5
        diff = 5 - remainder

        if (diff <= 2) and (g+diff > 38):
            rounded_grades.append(g + diff)
        else:
            rounded_grades.append(g)
    return rounded_grades


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # grades_count = int(input().strip())

    grades = [4, 73, 67, 38, 33]

    # for _ in range(grades_count):
    #     grades_item = int(input().strip())
    #     grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
