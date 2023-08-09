import sys
from heapq import heappop,heappush
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
minq = []
maxq = []
visited = defaultdict(bool)

for _ in range(n):
    p,l = map(int, input().split())
    heappush(minq,[l,p])
    heappush(maxq,[-l,-p])
    visited[p] = True # 방문 처리

m = int(input())
for _  in range(m):
    op = input().split()
    if op[0]=='recommend':
        if op[1]=='1':
            while not visited[-maxq[0][1]]: # 방문된 것이 맞는 것을 찾을 때까지 pop
                heappop(maxq)
            print(-maxq[0][1])
        else:
            while not visited[minq[0][1]]:
                heappop(minq)
            print(minq[0][1])
    elif op[0]=='solved':
        visited[int(op[1])] = False # 방문 취소 처리 
    else:
        P = int(op[1])
        L = int(op[2])
        # 같은 번호의 다른 난이도 문제가 삽입되어 이미 죽은 문제인데 True로 나와 출력되는 것을 방지.
        while not visited[-maxq[0][1]]:
            heappop(maxq)
        while not visited[minq[0][1]]:
            heappop(minq)
        visited[P] = True
        heappush(maxq,[-L,-P])
        heappush(minq,[L,P])