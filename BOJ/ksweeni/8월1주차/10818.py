import sys
input = sys.stdin.readline
stack = []

for i in range(int(input())):
  op = input()
  if 'push' in op:
    o,n = op.split(' ')
    stack.append(int(n))
  elif 'pop' in op:
    print(stack.pop()) if stack else print(-1)
  elif 'top' in op:
    print(stack[-1]) if stack else print(-1)
  elif 'size' in op:
    print(len(stack))
  elif 'empty'in op:
    print(0) if stack else print(1)