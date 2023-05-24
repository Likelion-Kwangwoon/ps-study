import heapq
import sys
n = int(input())
heap = []

for i in range(n) :
  a = int(sys.stdin.readline())
  if a :
    heapq.heappush(heap, (-a, a))
  else :
    if len(heap) >= 1:
      print(heapq.heappop(heap)[1])
    else :
      print(0)