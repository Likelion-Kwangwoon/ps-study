import sys
input = sys.stdin.readline
a,b = map(int,input().split(' '))
stack = []

for i in range(1,b+1):
  num = a*i
  stack.append(int(str(num)[::-1]))
print(max(stack))

