import sys
T = int(sys.stdin.readline())

for i in range(T):
    sticker = []
    n = int(sys.stdin.readline())
    for j in range(2):
        sticker.append(list(map(int,sys.stdin.readline().split())))

    if n == 1:
        print(max(sticker[0][0],sticker[1][0]))
        continue

    dp = [[ 0 for i in range(n)] for j in range(2)]
    #base case
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    dp[0][1] = sticker[0][1] + sticker[1][0]
    dp[1][1] = sticker[1][1] + sticker[0][0]
    #bottom up
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1]+ sticker[0][i] ,dp[1][i-2]+ sticker[0][i],dp[0][i-2]+ sticker[0][i])
        dp[1][i] = max(dp[0][i-1]+ sticker[1][i] ,dp[0][i-2]+ sticker[1][i], dp[1][i-2]+ sticker[1][i])
    
    print(max(max(dp[0]),max(dp[1])))