# Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros.
# Print the decimal value of each fraction on a new line.
#
# For example, given the array arr = [1, 1, 0, -1, -1]  there are 5  elements, two positive, two negative and one zero.
# Their ratios would be 2/5 = 0.400000, 2/5 =  0.400000 and 1/5 = 0.200000. It should be printed as
#
# 0.400000
# 0.400000
# 0.200000

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    print([x for x in arr if x > 0])
    print(format(len([x for x in arr if x > 0]) / n, ".6f"))
    print(format(len([x for x in arr if x < 0]) / n, ".6f"))
    print(format(len([x for x in arr if x == 0]) / n, ".6f"))


if __name__ == '__main__':
    n = int(input())

    arr = [1, 1, 2, 3, 4, 5, 0, 0, 0, -1, -2, -3]

    plusMinus(arr)
