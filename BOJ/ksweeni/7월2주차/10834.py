import sys
input = sys.stdin.readline
rd = 0
rn = 1

for i in range(int(input())):
    num = list(map(int,input().split()))
    rn = int(rn * num[1]/num[0])
    rd = (rd + num[2]) % 2

print(rd, rn)