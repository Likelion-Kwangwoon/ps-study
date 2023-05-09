T = int(input())
block = [[0,0], [0,3], [0,6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6,6]]
for t in range(1, T+1) :
  sudoku = [list(map(int,input().split())) for _ in range(9)]
  sudoku_t = list(zip(*sudoku))
  flag = True
  for i in range(9) :
    if len(set(sudoku[i])) != 9 :
      flag = False
      break
    if len(set(sudoku_t[i])) != 9 :
      flag = False
      break
    tmp = list()
    for j in range(block[i][0], block[i][0]+3) :
      for k in range(block[i][1], block[i][1]+3) :
        tmp.append(sudoku[j][k])
    
    if len(set(tmp)) != 9 :
      flag = False
      break
  
  if flag :
    print(f"#{t} 1")
  else :
    print(f"#{t} 0")