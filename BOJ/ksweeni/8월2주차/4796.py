import sys
stack = []
while(True):
  l,p,v = map(int, sys.stdin.readline().split(' '))
  if l == 0 and p ==0 and v == 0 :
    break
  mod = v%p
  if mod > l:
    mod = l
  stack.append((v//p)*l+mod)

for i in range(len(stack)):
  print('Case %d: %d'%(i+1, stack[i]))