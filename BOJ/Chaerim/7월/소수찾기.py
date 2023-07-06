import math
n=int(input())
arr = list(map(int,input().split()))
cnt = 0
for i in arr:
    flag = True
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                flag = False
        if flag:
            cnt += 1
print(cnt)
