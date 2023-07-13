n, m = map(int, input().split())

num = sorted(list(set(map(int, input().split()))))

ans = list()

def backtracking(d) :
  if d == m :
    print(" ".join(map(str, ans)))
    return
  for i in range(len(num)) :
    if d == 0 or ans[-1] <= num[i] :
      ans.append(num[i])
      backtracking(d + 1)
      ans.pop()

backtracking(0)