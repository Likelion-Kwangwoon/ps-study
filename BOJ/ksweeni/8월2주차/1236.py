import sys
n,m = map(int,sys.stdin.readline().split(' '))
stack = []
a,b = 0, 0
for i in range(n):
  stack.append(sys.stdin.readline().rstrip())

for i in range(n):
  if 'X' not in stack[i]:
    a+=1
    
for j in range(m):
  if "X" not in [stack[i][j] for i in range(n)]:
    b += 1

print(max(a,b))