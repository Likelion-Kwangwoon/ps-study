N = int(input())
for i in range(1,N+1):
    li = list(map(int,str(i)))
    res = i + sum(li)
    if res == N:
        print(i)
        break
    if i == N:
        print(0)
