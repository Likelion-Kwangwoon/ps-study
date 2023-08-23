t = int(input())
for _ in range(t) :
  num = input()
  data = []
  result = 0
  for i in range(len(num)) :
    if int(num[i]) not in data :
      result += 1
      data.append(int(num[i]))
  print(result)