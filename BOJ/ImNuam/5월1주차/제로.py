count = int(input())   
stack = []
sum = 0
for i in range(count):
    add = int(input())
    if add !=0:
        stack.append(add)
        sum += add
    else:
        sum -= stack.pop()
print(sum)