import sys
n = int(sys.stdin.readline())

stack = []
answer = []

flag = True
index = 1

for i in range(n):
  num = int(input())
  while index <= num:
    answer.append('+')
    stack.append(index)
    index+=1
  if stack[-1] == num:
    stack.pop()
    answer.append('-')
  else:
    print('NO')
    flag = False
    break;
  
if flag == True:
  for a in answer:
    print(a)