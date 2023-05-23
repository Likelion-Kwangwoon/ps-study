import sys
arr = []
size= 0
front=0
cnt = int(input())
for _ in range(cnt):
    command = sys.stdin.readline().split()
    if command[0] == "push" :
        arr.append(command[1])
        size+=1
    if command[0] == "pop":
        if size -front ==0:
            print(-1)
        else:
            print(arr[front])
            front+=1
    if command[0] == "size" :
        print(size-front)
    if command[0] == "empty":
        if size-front ==0:
            print(1)
        else :
            print(0)
    if command[0] == "back":
        if size-front==0:
            print(-1)
        else:
            a=arr.pop()
            print(a)
            arr.append(a)
    if command[0] == "front":
        if size-front==0:
            print(-1)
        else:
            print(arr[front])