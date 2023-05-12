from collections import deque
n, k = map(int, input().split())
dq = deque()
for i in range(1,n+1):
    dq.append(i)
arr = []

while len(dq) > 0:
    for _ in range(0,k-1):
        dq.append(dq.popleft())
    arr.append(dq.popleft())

print("<"+str(arr)[1:-1]+">")

#1158