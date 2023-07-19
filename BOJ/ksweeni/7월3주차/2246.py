condo = []
for i in range(int(input())):
  d,c = map(int,input().split(' '))
  condo.append([d,c])
condo=sorted(condo)
money = 10001
answer = 0
for i in condo:
  cost = i[1]
  if cost < money:
    money = cost
    answer+=1

print(answer)