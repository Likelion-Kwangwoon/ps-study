from collections import deque
m, n = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(tomato, m, n) :
  q = deque()
  
  for i in range(n) :
    for j in range(m) :
      if tomato[i][j] == 1 :
        q.append([i,j,0])
  while q :
    x, y, d = q.popleft()
    for i in range(4) :
      if (0 <= x+dx[i] < n )and (0 <= y+dy[i] < m) :
        if tomato[x+dx[i]][y+dy[i]] == 0 :
          q.append((x+dx[i],y+dy[i], d+1))
          tomato[x+dx[i]][y+dy[i]] = d+1
  lt = float('inf')
  mt = 0
  for l in tomato :
    mt = max(max(l), mt)
    if 0 in l :
      return -1
  if mt == 1 :
    return 0
  return mt

print(bfs(tomato, m, n))