n, m = map(int, input().split())

num = list(map(int, input().split()))

num.sort()
box = list()
def backtracking(d, s) :
  if d == m :
    print(' '.join(map(str, box)))
    return
  for i in range(s, n) :
    box.append(num[i])
    backtracking(d + 1, i)
    box.pop()

backtracking(0, 0)