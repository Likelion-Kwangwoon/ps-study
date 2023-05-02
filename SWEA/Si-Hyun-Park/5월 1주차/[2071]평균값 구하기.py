T = int(input())

for i in range(1, T + 1):
  num = list(map(int, input().split()))
  mean = round(sum(num) / 10)
  print("#{} {}".format(i, mean))
