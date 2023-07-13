n,m = map(int,input().split(' '))
num = [ i+1 for i in range(n) ]
for i in range(m):
  a,b = map(int,input().split(' '))
  num[a-1] , num[b-1] = num[b-1], num[a-1]
print(*num)