n = int(input())
grape = []

for i in range(n):
    grape.append(int(input()))


if n == 1:
    print(grape[0])
    exit()
if n == 2 :
    print(grape[0]+grape[1])
    exit()
if n == 3:
    print(max(grape[0]+ grape[1], grape[1]+grape[2],grape[0] + grape[2]))
    exit()


dp = {}
# base case
dp[0] = grape[0]
dp[1] = grape[0] + grape[1]
dp[2] = max(grape[0]+ grape[1], grape[1]+grape[2],grape[0] + grape[2])

# bottom up
for i in range(3, n):
    dp[i] = max(dp[i-3] + grape[i-1] + grape[i], dp[i-2]  + grape[i], dp[i-1])


print(max(dp.values()))