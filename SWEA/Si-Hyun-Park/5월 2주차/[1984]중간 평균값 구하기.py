T = int(input())

for t in range(1, T+1):
  score = list(map(int, input().split()))
  ans = round((sum(score) - max(score) - min(score)) / 8)
  
  print(f"#{t} {ans}")
  