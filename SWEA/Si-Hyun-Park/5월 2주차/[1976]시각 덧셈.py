T = int(input())

for tc in range(1, T+1) :
  t1, m1, t2, m2 = map(int, input().split())
  
  t = t1 + t2
  m = m1 + m2
  
  n = 0
  
  while m > 60 :
    n += 1
    m -= 60
  
  t += n
  n = 0
  while t > 12 :
    n += 1
    t -= 12
  
  print(f"#{tc} {t} {m}")