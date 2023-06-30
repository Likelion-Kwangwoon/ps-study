N = int(input())


dp = {}

# base case
dp[1] = 1
dp[2] = 1

#bottom up
for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])
