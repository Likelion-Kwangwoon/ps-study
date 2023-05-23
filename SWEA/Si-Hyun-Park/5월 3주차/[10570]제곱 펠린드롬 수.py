T = int(input())

for t in range(1, T+1) :
  a, b = map(int, input().split())
  p = [1, 4, 9, 121, 484]
  
  cnt = 0
  for i in range(5):
    if a <= p[i] <= b :
      cnt += 1
  
  print(f"#{t} {cnt}")