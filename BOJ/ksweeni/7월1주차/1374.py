import sys
import heapq
input = sys.stdin.readline

n = int(input())
hpq = []
table = []

for i in range(n):
    num, start, end = map(int, input().split())
    heapq.heappush(hpq, (start, end, num))

for i in range(n):
    s, e, num = heapq.heappop(hpq)

    if len(table) == 0:
        heapq.heappush(table, (e, s, num))
        continue

    te, ts, tnum = heapq.heappop(table)

    if te > s:
        heapq.heappush(table, (te, ts, tnum))
    heapq.heappush(table, (e, s, num))

print(len(table))