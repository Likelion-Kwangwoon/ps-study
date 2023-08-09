from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
dq = deque(enumerate(map(int,input().split())))
li = []
while dq:
    idx, paper = dq.popleft()
    li.append(idx+1)

    dq.rotate(-(paper-1)) if paper > 0 else dq.rotate(-paper)

print(*li)
