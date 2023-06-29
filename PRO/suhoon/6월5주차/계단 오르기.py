N = int(input())

stair = []

for i in range(N):
    stair.append(int(input()))


dp = {}
if N <= 2:
    print(sum(stair))
    exit()

# base case
dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

for i in range(3, N):
    dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i])


print(dp[N-1])
