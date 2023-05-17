T = int(input())

for t in range(1, T+1) :
  n = int(input())
  gdp = list(map(int, input().split()))
  avg = sum(gdp) // n
  cnt = 0
  for p in gdp :
    if p <= avg :
      cnt += 1
  print(f"#{t} {cnt}")