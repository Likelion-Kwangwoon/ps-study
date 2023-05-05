from copy import deepcopy

a, b ,N = input().split()
N = int(N)
board = [[0 for i in range(8)] for j in range(8)]
a = list(a)
b = list(b)
a[0] = ord(a[0])-64
b[0] = ord(b[0])-64

a = list(map(int, a))
b = list(map(int, b))
a[0], a[1] = a[1] ,a[0]
b[0], b[1] = b[1] ,b[0]
# print("king:"+ a[1] + str(a[0]))
# print("dol:" + b[1] + str(b[0]))


for i in range(N):
    temp_a = deepcopy(a)
    temp_b = deepcopy(b)
    command = input()
    flag = False

    if command == "R":
        temp_a[1] += 1
        temp_b[1] += 1
    elif command == "L":
        temp_a[1] -= 1
        temp_b[1] -= 1
    elif command == "B":
        temp_a[0] -= 1
        temp_b[0] -= 1
    elif command == "T":
        temp_a[0] += 1
        temp_b[0] += 1
    elif command == "RT":
        temp_a[0] += 1
        temp_b[0] += 1
        temp_a[1] += 1
        temp_b[1] += 1
    elif command == "LT":
        temp_a[0] += 1
        temp_b[0] += 1
        temp_a[1] -= 1
        temp_b[1] -= 1
    elif command == "RB":
        temp_a[0] -= 1
        temp_b[0] -= 1
        temp_a[1] += 1
        temp_b[1] += 1
    elif command == "LB":
        temp_a[0] -= 1
        temp_b[0] -= 1
        temp_a[1] -= 1
        temp_b[1] -= 1

    for i,j in zip(temp_a, temp_b):
        if i >= 9 or i< 1 or j >=9 or j <1:
            flag = True
    
    if flag == False:
        a = deepcopy(temp_a)
        b = deepcopy(temp_b)
            

a[0], a[1] = a[1] ,a[0]
b[0], b[1] = b[1] ,b[0]
print(a)
print(b)




