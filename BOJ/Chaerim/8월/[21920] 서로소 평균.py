import sys
input = sys.stdin.readline
N=int(input())
li = list(map(int,input().split()))
X=int(input())

def gcd(a,b):
    a,b=max(a,b),min(a,b)
    while b!=0:
        a,b=b,a%b
    return a
def lcm(a,b):
    a,b=max(a,b),min(a,b)
    return (a*b) //gcd(a,b)

average = []

for i in li:
    if gcd(X,i) == 1 and lcm(X,i) == X*i and i != X:
        average.append(i)
        
#표준 오차
print('{:.6f}'.format(sum(average)/len(average)))