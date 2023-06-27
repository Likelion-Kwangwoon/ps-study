N = int(input())

A=list(map(int, input().split()))

#Base case
dp= [1 for _ in range(N)]

#bottom up
#조건에 맞는다면 현재 dp값을 이전 dp값을 이용해 업데이트
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j] :
            dp[i] = max(dp[i] ,dp[j]+1)

print(max(dp))