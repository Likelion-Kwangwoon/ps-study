import math

def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

M = int(input())
N = int(input())
tot = 0
mini = 10000

for i in range(M,N+1):
    if isPrime(i):
       tot += i
       if mini >= i:
           mini = i

if tot == 0:
    print(-1)
else:
    print(tot)
    print(mini)

