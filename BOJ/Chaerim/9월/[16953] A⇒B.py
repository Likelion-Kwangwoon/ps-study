A,B = map(int,input().split())
cnt = 0

while A < B:
    if B % 2 == 0:
        B //= 2
        cnt += 1
    else:
        text = str(B)
        if text[-1] != '1':
            break
        else:
            B = int(text[:-1])
            cnt += 1

if A == B:
    print(cnt+1)
else:
    print(-1)