#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here

    # AM or PM
    day_or_night = s[8:]

    # Get the hour
    hour = int(s[:2])

    #print(day_or_night)

    if day_or_night == 'AM':
        if hour == 12:
            str_hour = '0'
        else:
            str_hour = str(hour)
    elif day_or_night == 'PM':
        if hour != 12:
            hour = hour + 12
        str_hour = str(hour)

    if int(str_hour) < 10:
        str_hour = '0' + str_hour

    new_time = str_hour + s[2:8]
    #print(new_time)
    return new_time

if __name__ == '__main__':

    s = '12:40:22AM'

    result = timeConversion(s)

