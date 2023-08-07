import sys
input = sys.stdin.readline

n = int(input())

stack = []
circle = []
for i in range(n):
  x,r = map(int, input().split(' '))
  stack.append((x-r,i)) # 원의 시작점과 순서
  stack.append((x+r,i)) # 원의 끝점과 순서
stack.sort()

for s in stack:
  if circle:
    if circle[-1][1] == s[1]:
      circle.pop()
    else:
      circle.append(s)
  else:
    circle.append(s)

print('NO') if circle else print('YES')