from collections import deque
import sys
input = sys.stdin.readline
dq = deque()
N = int(input())

for i in range(N):
    s = input().rstrip()
    if s == "pop_front":
        print(-1) if not dq else print(dq.popleft())
    elif s == "pop_back":
        print(-1) if not dq else print(dq.pop())
    elif s == "empty":
        print(1) if not dq else print(0)
    elif s == "front":
        print(dq[0]) if dq else print(-1)
    elif s=="back":
        print(dq[-1]) if dq else print(-1)
    elif s =="size":
        print(len(dq))
    else:
        dq.appendleft(s[11:]) if s[5] == 'f' else dq.append(s[10:])