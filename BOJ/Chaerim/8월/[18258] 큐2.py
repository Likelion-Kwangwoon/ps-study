import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
dq = deque()

for i in range(N):
    str = input().rstrip()

    if str == 'size':
        print(len(dq))
    elif str == 'empty':
        if not dq:
            print(1)
        else:
            print(0)
    elif str == 'front':
        if not dq:
            print(-1)
        else:
            print(dq[0])
    elif str == 'back':
        if not dq:
            print(-1)
        else:
            print(dq[-1])
    elif str == 'pop':
        if not dq:
            print(-1)
        else:
            print(dq.popleft())
    else:
        dq.append(str[5:])
