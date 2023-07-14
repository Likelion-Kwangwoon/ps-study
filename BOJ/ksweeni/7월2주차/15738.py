a,k,m = map(int, input().split())
arr = list(map(int,input().split()))
cur = k

for i in range(m):
    num = int(input())
    if num > 0 and cur <= num:
        cur = abs(cur - (num + 1))
    elif num < 0 and cur > num+a:
        cur = abs(a - cur + 1 + (a+num))
    else:
        continue
print(cur)