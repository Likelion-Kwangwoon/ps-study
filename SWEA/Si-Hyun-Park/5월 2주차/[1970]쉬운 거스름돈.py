T = int(input())
casher = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for t in range(1, T+1) :
  m = int(input())
  ans = list()
  for cash in casher :
    ans.append(m // cash)
    m = m - ans[-1]*cash
  print(f"#{t}")
  print(*ans)
  