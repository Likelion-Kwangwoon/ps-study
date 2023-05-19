#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
  # Write your code here
  ans = list()
  
  for i in range(1,n+1) :
    tmp = ""
    tmp += " "*(n-i)
    tmp += "#"*i
    ans.append(tmp)
  print(*ans, sep="\n")

if __name__ == '__main__':
  n = int(input().strip())

  staircase(n)
