import sys, heapq
input = sys.stdin.readline
hq = []
N=int(input())
for i in range(N):
    num = int(input())
    if num == 0:
        if not hq:
            print(0)
        else:
            print(heapq.heappop(hq)[1])
    else:
        heapq.heappush(hq, (abs(num), num))