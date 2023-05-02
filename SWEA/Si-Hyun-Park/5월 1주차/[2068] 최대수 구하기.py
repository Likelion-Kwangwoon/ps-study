T = int(input())

for i in range(1, T+1) :
  print("#{} {}".format(i, max(list(map(int, input().split())))))