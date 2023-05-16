T = int(input())

for t in range(1, T+1) :
  n = int(input())
  market = list(map(int, input().split()))
  max_price = market[-1]
  profit = 0
  
  for i in range(n-2, -1, -1) :
    if market[i] >= max_price :
      max_price = market[i]
    else :
      profit += max_price - market[i]
  
  print(f"#{t} {profit}")