import sys
input = sys.stdin.readline
N,B= input().split()
N = N[::-1] # 수 뒤집기 n**0부터 풀수있도록
B = int(B)
table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tot = 0
for i in range(len(N)):
    tot += (table.index(N[i])) * (B**i)
print(tot)