n,m = map(int, input().split(' '))
ball = [ i+1 for i in range(n)]
for _ in range(m):
  a,b = map(int, input().split(' '))
  ball[a-1], ball[b-1] = ball[b-1], ball[a-1]
print(*ball)