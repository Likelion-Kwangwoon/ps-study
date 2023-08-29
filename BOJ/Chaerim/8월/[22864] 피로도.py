A,B,C,M = map(int,input().split())
piro, time = 0,0
work = 0
while time < 24:
    time += 1
    if piro + A > M:
        piro -= C
        if piro < 0:
            piro = 0
    else:
        piro += A
        work += B
print(work)