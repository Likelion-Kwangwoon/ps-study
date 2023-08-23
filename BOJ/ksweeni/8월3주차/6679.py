import sys
input = sys.stdin.readline

def decToK(n,k):
    ans=0
    while n>0:
        ans+=n%k
        n=n//k
    return ans
 
for i in range(2992,10000):
    ten=decToK(i,10)
    twe = decToK(i, 12)
    six = decToK(i, 16)
    if ten==twe and twe==six : print(i)