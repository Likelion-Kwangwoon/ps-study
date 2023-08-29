n=int(input())

def gcd(a,b):
    a,b = max(a,b), min(a,b)
    while b != 0:
        a,b = b, a%b
    return a

def lcm(a,b):
    a,b = max(a,b), min(a,b)
    return (a*b) // gcd(a,b)

for _ in range(n):
    A,B = map(int,input().split())
    print(lcm(A,B))