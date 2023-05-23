def palindrome(word, l) :
  if l % 2 == 0 :
    if word[:l//2] == "".join(reversed(word[l//2:])) :
      return 1
    else : return 0
  else :
    if word[:l//2] == "".join(reversed(word[(l//2)+1:])) :
      return 1
    else : return 0
def solve(board, length) :
  cnt = 0
  for i in range(8) :
    for j in range(8-length+1):
      word = board[i][j:j+length]
      cnt += palindrome(word,length)
  return cnt


for i in range(1, 11) :
  length = int(input())
  
  board = [input() for _ in range(8)]
  
  cnt = solve(board, length)
  
  r_board = ["".join(list(x)) for x in zip(*board)]
  cnt += solve(r_board, length)
  
  print(f"#{i} {cnt}")
  