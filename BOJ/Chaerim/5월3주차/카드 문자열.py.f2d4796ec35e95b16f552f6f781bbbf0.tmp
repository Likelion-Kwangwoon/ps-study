from collections import deque
t = int(input())

dq1 = deque()
dq2 = deque()
arr = []
for _ in range(t):
    n = int(input())
    arr = list(input().split())
    for i in arr:
        dq1.append(i)
    for j in range(len(dq1)):
        if not dq2:
            dq2.append(dq1.popleft())
        else:
            temp = dq1.popleft()
            if ord(dq2[0]) < ord(temp):
                dq2.append(temp)
            else:
                dq2.appendleft(temp)

    for k in range(len(dq2)):
        print(dq2.popleft(), end="")
  
#13417 data structure