import sys
import heapq
cnt = int(input())
heap = []
for _ in range(cnt):
    item = int(sys.stdin.readline())
    if item:
        heapq.heappush(heap, (-item,item))
    else:
        if len(heap) >=1:
            print(heapq.heappop(heap)[1])
        else:
            print(0)