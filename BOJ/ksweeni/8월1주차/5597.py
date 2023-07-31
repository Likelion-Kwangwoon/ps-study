stu = []
for i in range(28):
  stu.append(int(input()))
no_li= []
for i in range(1,31):
  if stu.count(i)==0:
    no_li.append(i)
print(min(no_li))
print(max(no_li))