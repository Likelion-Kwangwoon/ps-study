from collections import deque
import sys
input = sys.stdin.readline
dq = deque()
N=int(input())
for i in range(N):
    dq.append(i+1)

while len(dq) != 1:
    dq.popleft()
    dq.rotate(-1) #반시계

print(dq.pop())