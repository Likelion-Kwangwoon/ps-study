n, m = map(int, input().split())

matrix = [[float('inf')] * (n+1) for _ in range(n+1)]

for _ in range(m) :
  a, b = map(int, input().split())
  matrix[a][b] = 1
  matrix[b][a] = 1

for i in range(1,n+1) :
  matrix[i][i] = 0
  
for k in range(1, n+1) :
  for i in range(1, n+1) :
    for j in range(1, n+1) :
      matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

bacon = float('inf')
ans = 0
for i in range(n, 0, -1) :
  s = sum(matrix[i][1:])
  if bacon >= s :
    bacon = s
    ans = i
print(ans)
