import sys
input = sys.stdin.readline
N=int(input())
road = list(map(int,input().split()))
cost = list(map(int,input().split()))

money = 0
m = cost[0]

for i in range(N-1):
    if cost[i] < m:
        m = cost[i]
    money += m * road[i]
print(money)