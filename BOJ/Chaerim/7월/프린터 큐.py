from collections import deque
t = int(input())
dq = deque()
for _ in range(t):
    n, m = map(int, input().split())
    dq = deque(list(map(int, input().split())))
    cnt =0
    while True:
        if dq[0] < max(dq):
            dq.rotate(-1)
            if m == 0:
                m = len(dq)-1
            else:
                m -= 1
        else:
            dq.popleft()
            cnt += 1
            m -= 1
            if m < 0:break
    print(cnt)
