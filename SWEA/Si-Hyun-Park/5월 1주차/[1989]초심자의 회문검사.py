T = int(input())

for t in range(1, T+1) :
  word = input().rstrip()
  test = word[::-1]
  if word == test :
    print("#{} 1".format(t))
  else :
    print("#{} 0".format(t))