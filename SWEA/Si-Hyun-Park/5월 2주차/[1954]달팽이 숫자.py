T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for t in range(1, T+1) :
  n = int(input())
  target = n ** 2
  snail = [[0 for j in range(n)] for i in range(n)]
  i, j, cnt = 0, 0, 1
  flag = 0
  
  snail[i][j] = cnt 
  cnt += 1
  
  while cnt <= target :
    ni, nj = (i + di[flag]), (j + dj[flag])
    if ( 0 <= ni < n ) and ( 0 <= nj < n ) and snail[ni][nj] == 0 :
      snail[ni][nj] = cnt
      i, j = ni, nj
      cnt += 1
    else :
      flag = ( flag + 1 ) % 4
  
  print(f"#{t}")
  
  for l in snail :
    print(*l)