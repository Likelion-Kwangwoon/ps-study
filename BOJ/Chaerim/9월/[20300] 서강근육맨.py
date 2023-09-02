import sys
input = sys.stdin.readline

N=int(input())
gen = list(map(int,input().split()))
gen.sort() #Nlog(N)

def fun(arr, t):
    for i in range(len(arr)//2):
        tmp2 = gen[i] + gen[-i-1]
        if tmp2 > t:
            t = tmp2
    return t

if len(gen)% 2 == 0:
    tmp = min(gen) + max(gen)
    gen.remove(max(gen))
    gen.remove(min(gen))
    print(fun(gen,tmp))
else:
    tmp = max(gen)
    gen.remove(max(gen))
    print(fun(gen,tmp))

