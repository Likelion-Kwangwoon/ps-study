n, m = map(int, input().split())

num = list(map(int, input().split()))

num.sort()
box = list()
def backtracking(d) :
  if d == m :
    print(' '.join(map(str, box)))
    return
  for i in range(n) :
    if num[i] in box:
      continue
    box.append(num[i])
    backtracking(d + 1)
    box.pop()

backtracking(0)