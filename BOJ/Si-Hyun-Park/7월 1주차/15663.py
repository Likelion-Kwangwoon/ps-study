n, m = map(int, input().split())

num = list(map(int, input().split()))

num.sort()
box = list()

visited = [0 for _ in range(n)]
def backtracking(d) :
  if d == m :
    print(' '.join(map(str, box)))
    return
  tmp = 0
  for i in range(n) :
    if (visited[i] == 0 and tmp != num[i]) :
      visited[i] = 1
      box.append(num[i])
      tmp = num[i]
      backtracking(d + 1)
      box.pop()
      visited[i] = 0

backtracking(0)