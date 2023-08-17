import sys
input = sys.stdin.readline

a,b=map(int, input().split())
for i in range(1,10001):
    for j in range(1,10001):
        if i*j==a+b and a==2*i+2*j-4 :
            print(max(i,j),min(i,j))
            exit()