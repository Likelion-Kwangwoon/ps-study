import math
N=int(input())

def eratosthenes(N):
    prime = []
    i = 2
    while i <= N:
        if N % i == 0:
            N /= i
            prime.append(i)
        else:
            i += 1
    return sorted(prime)

if N== 1:
    print("")
else:
    res = eratosthenes(N)
    for i in res:
        print(i)