import math
import sys
input=sys.stdin.readline

t = int(input())

for i in range(t):
  a,b = map(int,input().split(' '))
  gcd = math.gcd(a,b)
  lcm = a*b / gcd
  print(int(lcm))