N , M = map(int,input().split())

brand6 = []
brand1 = []
for i in range(M):
    a, b = map(int,input().split())
    brand6.append(a)
    brand1.append(b)

brand6.sort()
brand1.sort()
k = N // 6
t = N %  6

answer = min(brand1[0]*N,brand6[0]*k + brand1[0]*t,brand6[0]*(k+1))
print(answer)