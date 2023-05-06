T = int(input())

def solve(board, n, k) :
  answer = 0
  for i in range(n) :
    cnt = 0
    for j in range(n) :
      if board[i][j] == "1" :
        cnt += 1
      if board[i][j] == "0" or j == (n-1) :
        if cnt == k :
          answer += 1
        if board[i][j] == "0":
          cnt = 0
  return answer
        
for t in range(1,T+1) :
  n, k = map(int, input().split())
  ans = 0
  board = list()
  for _ in range(n):
    board.append(list(input().split()))
    
  ans += solve(board, n, k)
  ans += solve(list(zip(*board)), n, k)
  
  print("#{} {}".format(t, ans))