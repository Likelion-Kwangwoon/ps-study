T = int(input())

for t in range(1,T+1) :
  n = int(input())
  if n % 2 == 0 :
    ans = (n // 2) * -1
  else :
    ans = ((n+1) // 2)

  print("#{} {}".format(t, ans))