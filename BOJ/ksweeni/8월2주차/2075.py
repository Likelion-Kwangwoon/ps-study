import heapq
import sys

n = int(sys.stdin.readline())
q = []

for i in range(n):
  num = list(map(int, sys.stdin.readline().split(' ')))
  if i == 0:
    for n in num:
      heapq.heappush(q,n)
  else:
    for n in num:
      if n > q[0]:
        heapq.heappop(q)
        heapq.heappush(q,n)

print(q[0])