N,K = map(int,input().split())
cnt=0
for i in range(60):
    if i <10:
        i = '0'+str(i)
    for j in range(60):
        if j < 10:
            j = '0'+str(j)
        for k in range(N+1):
            if k <10:
                k = '0' + str(k)
            tmp = str(i)+str(j)+str(k)
            if str(K) in tmp:
                cnt += 1
print(cnt)