A,B = map(int,input().split())

def gcd(a,b):
    a,b = max(a,b), min(a,b)

    while b != 0:
        a,b = b, a%b
    return a

def lcm(a,b):
    a,b = max(a,b), min(a,b)
    return (a*b) // gcd(a,b)

print(gcd(A,B))
print(lcm(A,B))