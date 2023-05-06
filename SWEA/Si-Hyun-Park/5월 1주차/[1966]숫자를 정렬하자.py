T = int(input())

for t in range(1, T+1) :
  n = int(input())
  row = list(map(int, input().split()))
  row.sort()
  print("#{}".format(t), end=" ")
  for r in row :
    print(r, end=" ")
  print()