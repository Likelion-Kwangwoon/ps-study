from collections import deque
for _ in range(10) :
  n = int(input())
  pw = deque(map(int, input().split()))
  factor = [1,2,3,4,5]
  f = 0
  while True :
    tmp = pw.popleft() - factor[f]
    pw.append(tmp)
    if tmp <= 0 :
      pw[7] = 0
      break
    f += 1
    if f > 4 :
      f = 0
      
    
  print(f"#{n} ",end="")
  print(*list(pw))
  