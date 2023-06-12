from collections import deque
n = int(input())

apart = [list(map(int, input())) for _ in range(n)]
ans = list()

def bfs(i, j):
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
  q = deque([(i,j)])
  apart[i][j] = 0
  cnt = 1
  while q :
    y, x = q.popleft()
    for k in range(4) :
      if 0 <= y+dy[k] < n and 0 <= x+dx[k] < n and apart[y+dy[k]][x+dx[k]] == 1:
        apart[y+dy[k]][x+dx[k]] = 0
        q.append((y+dy[k], x+dx[k]))
        cnt += 1
  return cnt
  
for i in range(n) :
  for j in range(n) :
    if apart[i][j] == 1 :
      ans.append(bfs(i,j))
ans.sort()
print(len(ans))
print(*ans, sep="\n")
