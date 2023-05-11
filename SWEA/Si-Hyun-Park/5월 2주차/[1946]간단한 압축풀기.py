T = int(input())

for t in range(1, T+1) :
  n = int(input())
  text = ""
  for i in range(n) :
    c, k = input().split()
    for _ in range(int(k)) :
      text += c
  print(f"#{t}")
  for idx, a in enumerate(text):
    print(a,end="")
    if idx % 10 == 9  :
      print()
  print()