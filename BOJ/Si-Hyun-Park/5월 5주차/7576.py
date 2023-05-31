from collections import deque
m, n = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(tomato, m, n) :
  q = deque()
  
  for i in range(m) :
    for j in range(n) :
      if tomato[i][j] == 1 :
        q.append([i,j,0])
  
  while q :
    x, y, d = q.popleft()
    for i in range(4) :
      if 0 < x+dx[i] < m and 0 < y+dy[i] < n :
        if tomato[x+dx[i]][y+dy[i]] == 0 :
          q.append((x+dx[i],y+dy[i], d+1))
          tomato[x+dx[i]][y+dy[i]] = d+1
  lt = float('inf')
  mt = 0
  for l in tomato :
    lt = min(min(l), lt)
    mt = max(max(l), mt)
  
  if lt == 0 :
    return -1
  else :
    return mt

bfs(tomato, m, n)