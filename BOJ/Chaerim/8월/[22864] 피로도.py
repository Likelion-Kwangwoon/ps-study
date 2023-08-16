import sys
input = sys.stdin.readline

A,B,C,M = map(int,input().split())
work = 0
piro = 0
i =0

if A > M:
    print(0)
else:
    while i < 24:
        i += 1
        if piro + A <= M:
            work += B
            piro += A
        else:
            if piro - C < 0:
                piro = 0
            else:
                piro -= C
    print(work)