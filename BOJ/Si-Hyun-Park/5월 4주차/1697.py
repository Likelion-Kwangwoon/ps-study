from collections import deque
n, k = map(int, input().split())

def bfs(n, k) :
  visited = [False for _ in range(100001)]
  visited[n] = True
  q = deque([(n,0)])
  while q :
    t, d= q.popleft()
    if t == k :
      return d
    else :
      if t < 100000 :
        if not visited[t+1] :
          visited[t+1] = True
          q.append((t+1, d+1))
      if t > 0:
        if not visited[t-1] :
          visited[t-1] = True
          q.append((t-1, d+1))
      if t <= 50000 :
        if not visited[t*2] :
          visited[t*2] = True
          q.append((t*2, d+1))

print(bfs(n,k))