from collections import deque
n, m = map(int, input().split())

campus = list()
q = deque()
for i in range(n) :
  t = input()
  if "I" in t :
    q.append((i, t.index("I")))
  campus.append(list(t))
  
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0
while q :
  y, x = q.popleft()
  
  for i in range(4) :
    if 0 <= y + dy[i] < n and 0 <= x + dx[i] < m :
      if campus[y+dy[i]][x+dx[i]] == "O" :
        q.append((y+dy[i], x+dx[i])) 
      if campus[y+dy[i]][x+dx[i]] == "P" :
        q.append((y+dy[i], x+dx[i])) 
        cnt += 1
      campus[y+dy[i]][x+dx[i]] = "I"

if cnt :
  print(cnt)
else :
  print("TT")