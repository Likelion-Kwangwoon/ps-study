N=int(input())

def isPrime(x):
    if x == 1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def isPalindrome(x):
    x = str(x)
    x2 = x[::-1]
    if x == x2:
        return True
    else:
        return False

while True:
    if isPalindrome(N):
        if isPrime(N):
            print(N)
            exit(0)
    N +=1