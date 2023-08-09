import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []
for i in range(n):
  num = int(input())
  if num == 0 :
    if q:
      print(-1*heapq.heappop(q))
    else:
      print(0)
  else :
    heapq.heappush(q,-num)