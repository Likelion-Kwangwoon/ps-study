import sys
input = sys.stdin.readline

str = list(input().rstrip())
stack = []
ans = ''

for s in str:
  if s.isalpha():
    ans+=s
  elif s == '(':
    stack.append(s)
    
  elif s == '*' or s == '/':
    while stack and (stack[-1] == '*' or stack[-1] =='/'):
      ans+=stack.pop()
    stack.append(s)
       
  elif s == '+' or s == '-':
    while stack and stack[-1] != '(':
        ans += stack.pop()
    stack.append(s)
      
  elif s == ')':
    while stack and stack[-1] != '(':
        ans += stack.pop()
    stack.pop()
while stack:
  ans+=stack.pop()
print(ans)