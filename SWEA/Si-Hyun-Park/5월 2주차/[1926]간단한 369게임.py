n = int(input())

ans = list()

for i in range(1,n+1) :
  num = str(i)
  tmp = ""
  flag = False
  for a in num :
    if a == "3" or a == "6" or a == "9" :
      tmp += "-"
      flag = True
  if flag :
    ans.append(tmp)
  else :
    ans.append(num)

print(*ans)