import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
  str = input()
  stack = []
  for s in str:
    if s=='(':
      stack.append(s)
    elif s==')':
      if stack:
        stack.pop()
      else:
        print('NO')
        break
  else: 
    print("YES") if not stack else print("NO")