N = int(input())
if N == 1:
    print(9)
    exit()

#base case
dp = [[ 0 for i in range(10)] for j in range(N+1)]
for i in range(1,10):
    dp[1][i] = 1

#bottom up
for i in range(2, N+1):
    dp[i][0] = dp[i-1][1]
    for k in range(1 ,9):
        dp[i][k] = dp[i-1][k-1] + dp[i-1][k+1]
    dp[i][9] = dp[i-1][8]


ans = (sum(dp[N])) % 1000000000 
print(ans)