import sys
input = sys.stdin.readline
T=int(input())
#기존 방법은 시간복잡도에 걸리니까 유클리드 호제법을 써야한다.

def gcd(a,b): #유클리드 호제법은 기존 O(N)-> O(logN)까지 줄일 수있다.
    while b>0:
        a,b = b,a%b
    return a

def lcm(a,b):
    a,b = max(a,b), min(a,b)
    return (a*b) // gcd(a,b)

for _ in range(T):
    A,B = map(int,input().split())
    res = lcm(A,B)
    print(res)