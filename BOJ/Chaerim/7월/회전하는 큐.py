from collections import deque

n,m = map(int, input().split())
cnt = 0
arr = list(map(int, input().split()))
dq = deque()
for i in range(1,n+1):
    dq.append(i)

for item in arr:
    while True:
        if dq[0] == item:
            dq.popleft()
            break
        else:
            if dq.index(item) <= len(dq)//2:
                while dq[0] != item:
                    dq.append(dq.popleft())
                    cnt+=1
            else:
                while dq[0] != item:
                    dq.appendleft(dq.pop())
                    cnt+=1
print(cnt)
