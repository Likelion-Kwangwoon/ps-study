from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N,M = map(int,input().split())
    dq = deque(list(map(int,input().split())))
    n=0
    while dq:

        mx = max(dq)
        front = dq.popleft()
        M -= 1

        if mx == front:
            n += 1
            if M < 0:
                print(n)
                break
        else:
            dq.append(front)
            if M < 0:
                M = len(dq)-1