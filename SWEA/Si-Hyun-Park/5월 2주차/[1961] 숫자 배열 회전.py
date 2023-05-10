T = int(input())

for t in range(1, T+1) :
  n = int(input())
  matrix = list()
  for _ in range(n) :
    line = list(map(str, input().split()))
    matrix.append(line)
    
  matrix_90 = list()
  for i in range(n) :
    row = ""
    for j in range(n-1, -1, -1) :
      row += matrix[j][i]
    matrix_90.append(row)
  
  matrix_180 = list()
  for i in range(n-1, -1, -1) :
    row = ""
    for j in range(n-1, -1, -1) :
      row += matrix[i][j]
    matrix_180.append(row)
  
  matrix_270 = list()
  for i in range(n-1, -1, -1) :
    row = ""
    for j in range(n) :
      row += matrix[j][i]
    matrix_270.append(row)
  
  print("#{}".format(t))
  for i in range(n) :
    print(matrix_90[i], matrix_180[i], matrix_270[i])
    