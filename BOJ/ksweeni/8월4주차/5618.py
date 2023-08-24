from collections import defaultdict
import sys
input=sys.stdin.readline

dic = defaultdict(int)

n = int(input())

li = list(map(int, input().split(' ')))

for i in li:
  for x in range(1,i+1):
    if i%x == 0:
      dic[x]+=1

for d in dic:
  if dic[d] == n:
    print(d)