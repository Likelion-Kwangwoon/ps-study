a, b = map(int, input().split())

win = a - b

if win == 1 or win == -2 :
  print("A")
elif win == 2 or win == -1:
  print("B")