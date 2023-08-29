N,K = map(int,input().split())
arr = [True]*(N+1)
tmp = 0
for i in range(2,N+1):
    for j in range(i,N+1,i):
        if arr[j] == True:
            arr[j] = False
            tmp += 1
            if tmp == K:
                print(j)