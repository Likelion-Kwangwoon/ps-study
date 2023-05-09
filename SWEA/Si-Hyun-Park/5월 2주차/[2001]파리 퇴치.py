T = int(input())

for t in range(1, T+1) :
  n, m = map(int, input().split())
  wall = list()
  for i in range(n) :
    l = list(map(int, input().split()))
    wall.append(l)
  ans_list = list()
  for i in range(n-m+1) :
    for j in range(n-m+1) :
      fly = 0
      for x in range(m) :
        for y in range(m) :
          fly += wall[i+x][j+y]
      ans_list.append(fly)
  print(f"#{t} {max(ans_list)}")