import sys, heapq
input = sys.stdin.readline
hq, max_hq = [], []

def add(p,l):
    heapq.heappush(hq,(l,p)) #레벨으로 정렬해야하니 바꿔서 push
    heapq.heappush(max_hq,(-l,-p))
def solved(p):
    if p == hq[0][1]: #가장 쉽고 번호작은 문제
        heapq.heappop(hq)
    elif p == max_hq[0][1] * -1: #가장 어렵고 번호 큰 문제
        heapq.heappop(max_hq)
def recmd(n):
    if n == 1:
        print(max_hq[0][1] * -1)
    else:
        print(hq[0][1])

for i in range(int(input())):
    P, L = map(int,input().split())
    heapq.heappush(hq, (L, P))
    heapq.heappush(max_hq, (-L, -P))

for i in range(int(input())):
    cmd = list(input().split())
    if cmd[0] == 'add':
        add(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'solved':
        solved(int(cmd[1]))
    else:
        recmd(int(cmd[1]))