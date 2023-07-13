n,m = map(int,input().split(' '))
cnt = [ 0 for i in range(n) ]
for i in range(m):
  a,b = map(int,input().split(' '))
  cnt[a-1]+=1
  cnt[b-1]+=1
for i in cnt:
  print(i)