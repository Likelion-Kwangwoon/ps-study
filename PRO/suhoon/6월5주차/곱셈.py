A , B , C = map(int,input().split())

#분할정복(O(logN))

def dac(a,b,c):
    if b == 1:
        return a % c
    
    if b % 2 == 0:
        return (dac(a,b//2,c) ** 2)%c
    elif b % 2 == 1:
        return ((dac(a,b//2,c) ** 2)*a)%c


print(dac(A,B,C))