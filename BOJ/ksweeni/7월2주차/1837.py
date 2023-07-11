a, b= map(int, input().split())
flag = True
for i in range(2,b):
    if a % i == 0:
        print('BAD', i)
        flag = False
        break
if flag:
    print('GOOD')