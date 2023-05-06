T = int(input())

days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
for t in range(1, T+1) :
  m1, d1, m2, d2 = map(int, input().split())
  print("#{} {}".format(t, (d2 + days[m2-1]) - (d1+ days[m1-1]) + 1)) 