T = int(input())

def solve(n, m, a, b) :
  ans = 0
  for i in range(m-n+1) :
    tmp = 0
    for j in range(n) :
      tmp += a[j]*b[i+j]
    ans = max(ans, tmp)
  return ans
for t in range(1, T+1) :
  n, m = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  
  if n <= m :
    ans = solve(n, m, a, b)
  else:
    ans = solve(m, n, b, a)
  print("#{} {}".format(t, ans))
  
  