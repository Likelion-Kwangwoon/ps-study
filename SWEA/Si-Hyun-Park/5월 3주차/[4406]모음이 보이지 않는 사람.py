T = int(input())

for t in range(1, T+1) :
  word = input().rstrip()
  
  table = word.maketrans({
    'a': '',
    'e': '',
    'i': '',
    'o': '',
    'u': '',
  })
  print(f"#{t} {word.translate(table)}")