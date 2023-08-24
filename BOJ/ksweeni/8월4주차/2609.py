import math
import sys
input=sys.stdin.readline

a,b = map(int,input().split(' '))
gcd = math.gcd(a,b)
lcm = a*b / gcd
print(gcd)
print(int(lcm))