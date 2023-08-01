from itertools import combinations
import sys
input = sys.stdin.readline

answer = 0
num = [ int(input()) for _ in range(9)]

comb = list(combinations(num,7))

for i in comb:
  if(sum(i))==100 :
    for n in i:
      print(n)