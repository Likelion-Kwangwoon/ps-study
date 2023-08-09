import sys, heapq
input = sys.stdin.readline
N = int(input())
hq = []
for i in range(N):
    li = list(map(int,input().split()))
    for n in li:
        if len(hq) < N:
            heapq.heappush(hq,n)
        else:
            if hq[0] < n:
                heapq.heappop(hq)
                heapq.heappush(hq,n)
print(hq[0])
