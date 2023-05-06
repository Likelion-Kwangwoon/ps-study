N = int(input())
num = []
for i in range(N):
    a, b = map(int, input().split())
    num.append([a,b])


num.sort()
for item in num:
    print(*item)



