N = int(input())
flag = 0 
for i in range(N):
    sum = 0
    iList = list(str(i))
    for j in range(len(iList)):
        sum += int(iList[j])
    if sum + i == N:
        print(i)
        flag = 1
        break
if flag == 0:
    print(0)