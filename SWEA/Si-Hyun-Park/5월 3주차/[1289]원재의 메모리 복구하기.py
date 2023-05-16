T = int(input())

for t in range(1, T+1) :
  bina = input()
  cnt = 0
  flag = "0"
  for n in bina :
    if flag != n :
      cnt += 1
      flag = n
  
  print(f"#{t} {cnt}")
  