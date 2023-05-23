import heapq
import sys
N, K = map(int, sys.stdin.readline().split())
q = heapq()
bosuk = []
bags = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    bosuk.append((a,b))

for i in range(K):
    bags.append(int(sys.stdin.readline()))

bosuk.sort()
bags.sort()
#print(C)
sum =0

for bag in bags:

    while bosuk and bag >= bosuk[0][0]:






