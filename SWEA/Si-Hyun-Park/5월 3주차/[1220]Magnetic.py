from collections import deque 
for t in range(1, 11) :
  z = int(input())
  
  board = [list(map(int, input().split())) for _ in range(100)]
  
  board_t = list(zip(*board))
  cnt = 0
  for line in board_t :
    tmp = deque()
    for n in line :
      if n != 0 :
        tmp.append(n)
    while True :
      if tmp[0] == 2 :
        tmp.popleft()
      else : break
    while True :
      if tmp[-1] == 1 :
        tmp.pop()
      else : break
    flag = True
    for i in tmp :
      if i == 1 and flag == False :
        flag = True
      elif i == 2 and flag == True :
        cnt += 1
        flag = False
    
  print(f"#{t} {cnt}")
      