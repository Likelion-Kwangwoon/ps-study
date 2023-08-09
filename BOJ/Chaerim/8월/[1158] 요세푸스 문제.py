from collections import deque
import sys
input = sys.stdin.readline
dq = deque()
li = []
N,K = map(int,input().split())
for i in range(N):
    dq.append(i+1)

while dq:
  dq.rotate(-K+1)
  n = dq.popleft()
  li.append(str(n))
print("<"+', '.join(li)+">")