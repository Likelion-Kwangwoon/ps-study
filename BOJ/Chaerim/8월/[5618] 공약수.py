import sys
input = sys.stdin.readline
n=int(input())
li = list(map(int,input().split()))
#2개 또는 3개 주어짐
arr = [1]
def gcd(a,b):
    if b ==0:
        return a
    return gcd(b,a%b)

g = gcd(li[0], gcd(li[1],li[-1]))

for i in range(1,g//2+1): #시간복잡도에 걸릴까봐 이렇게 푼다고 한다.
    if g % i == 0:
        print(i)
print(g)

