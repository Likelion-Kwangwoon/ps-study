#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr, cnt):
    # Write your code here
    p = 0
    n = 0
    z = 0
    for a in arr :
      if a > 0 :
        p += 1
      elif a < 0:
        n += 1
      else :
        z += 1
    print(f"{p/cnt: .6f}")
    print(f"{n/cnt: .6f}")
    print(f"{z/cnt: .6f}")
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)
