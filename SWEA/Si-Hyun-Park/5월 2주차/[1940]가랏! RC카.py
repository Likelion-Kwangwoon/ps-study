T = int(input())

for t in range(1, T+1) :
  n = int(input())
  v = 0
  s = 0
  for _ in range(n) :
    i = input()
    if i == "0" :
      m = 0
    else :
      m, a = map(int, i.split())
    if m == 1 :
      v += a
    elif m == 2 :
      if v - a >= 0 :
        v -= a
      else :
        v = 0
    s += v
  print("#{} {}".format(t, s))

