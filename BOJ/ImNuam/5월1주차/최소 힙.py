import heapq
import sys
cnt = int(input())
heap=[]
for _ in range(cnt):
    n = int(sys.stdin.readline())
    if n!=0:
        heapq.heappush(heap, n)
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))