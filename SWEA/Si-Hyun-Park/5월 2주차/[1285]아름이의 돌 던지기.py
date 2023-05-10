T = int(input())

for t in range(1, T+1) :
  n = int(input())
  rock = list(map(lambda x: abs(int(x)), input().split()))
  rock.sort()
  ans = min(rock)
  cnt = 0
  for r in rock :
    if ans == r :
      cnt += 1
    else :
      break
  print("#{} {} {}".format(t, ans, cnt))