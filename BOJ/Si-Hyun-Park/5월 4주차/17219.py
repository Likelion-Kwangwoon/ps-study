n, m = map(int, input().split())

pw = dict()
for _ in range(n) :
  a, b = map(str, input().split())
  pw[a] = b
  

for _ in range(m) :
  site = input()
  print(pw[site])