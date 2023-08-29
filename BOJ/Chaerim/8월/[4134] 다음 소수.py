import sys
input = sys.stdin.readline
t=int(input())

def eratos(N):
    for i in range(2,int(N**0.5)+1):
        if N % i == 0:
            return False
    return True

for _ in range(t):
    n=int(input())
    while True:
        if n == 0 or n == 1:
            print(2)
            break
        if eratos(n):
            print(n)
            break
        else:
            n+=1