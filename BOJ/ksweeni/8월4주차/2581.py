import sys
input=sys.stdin.readline

def decimal(n):
  for i in range(2,n+1):
    if n%i == 0:
      if i == n:
        return True
      else:
        return False

m = int(input())
n = int(input())
li = []

for x in range(m,n+1):
  if (decimal(x)):
    li.append(x)
if len(li) == 0 :
  print(-1)
else:
  print(sum(li)) 
  print(min(li))