import sys
from itertools import combinations
input = sys.stdin.readline
t = int(input())
#가능한 모든쌍의 최대공약수의 합
def gcd(a,b):
    a,b = max(a,b),min(a,b)
    while b!=0:
        a,b=b,a%b
    return a

for _ in range(t):
    li = list(map(int,input().split()))
    li.remove(li[0])
    li2 = list(combinations(li,2))
    total = 0
    for i in range(len(li2)):
        total += gcd(li2[i][0],li2[i][1])
    print(total)