import sys

T = int(sys.stdin.readline())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]

ans = list()
def cut(x, y, T) :
  now = paper[x][y]
  for i in range(x, x+T) :
    for j in range(y, y+T) :
      if now != paper[i][j] :
        cut(x, y, T//2)
        cut(x, y+T//2, T//2)
        cut(x+T//2, y, T//2)
        cut(x+T//2, y+T//2, T//2)
        return
  if now == 0 :
    ans.append(0)
  else :
    ans.append(1)

cut(0,0,T)
print(ans.count(0))
print(ans.count(1))
    