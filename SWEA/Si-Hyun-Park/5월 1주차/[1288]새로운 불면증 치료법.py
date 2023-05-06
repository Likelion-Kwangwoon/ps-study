T = int(input())

for t in range(1,T+1) :
  n = int(input())
  num = n
  check = set(str(n))
  cnt = 1
  while(len(check) < 10) :
    n += num
    check.update(str(n))
    cnt += 1
  print("#{} {}".format(t, cnt*num))