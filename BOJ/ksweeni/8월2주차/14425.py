import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))

a = set()
b = []
count = 0

for i in range(n):
  a.add(input().strip())
  
for i in range(m):
  b.append(input().strip())

for new in b:
  if new in a:
    count+=1

print(count)