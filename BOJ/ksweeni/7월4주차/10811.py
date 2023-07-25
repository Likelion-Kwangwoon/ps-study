n,m = map(int,input().split(' '))
li = list(range(1,n+1))

for i in range(m):
  i,j=map(int,input().split(' '))
  temp = reversed(li[i-1:j])
  li[i-1:j]=temp

for i in range(n):
  print(li[i], end=' ')