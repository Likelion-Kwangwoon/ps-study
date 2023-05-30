import heapq
import sys
N, K = map(int, sys.stdin.readline().split())
heap = []
bosuk = []
bags = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    bosuk.append((a,b))

for i in range(K):
    bags.append(int(sys.stdin.readline()))

bosuk.sort()
bags.sort()

heapq.heappush(heap,4)





