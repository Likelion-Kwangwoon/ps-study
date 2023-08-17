import math
import sys
input = sys.stdin.readline
for _ in range(int(input())):
  car = input().rstrip().split('-')
  cal = 0
  index = len(car[0])-1
  for c in car[0]:
    cal +=int((ord(c)-65)*math.pow(26,index))
    index-=1
  if abs(cal-int(car[1])) <= 100:
    print('nice')
  else:
    print('not nice')