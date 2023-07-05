A = int(input())
X = int(input())


def Rec(a, b):
    if b == 1:
        return a * 1 %1000000007
    
    if b % 2 == 0:
        return Rec(a , b//2) ** 2 

    elif b % 2 ==1:
        return Rec(a, b // 2) **2 * a %1000000007
    

print(Rec(A,X))
