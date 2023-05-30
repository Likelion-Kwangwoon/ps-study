import heapq
import sys

n= int(sys.stdin.readline())
q = []
for i in range(n):
    x = int(sys.stdin.readline().strip())
    if x != 0:
        heapq.heappush(q,(abs(x), x))
    else: #x==0
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])
 #11286
