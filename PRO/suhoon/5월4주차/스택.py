import sys

N = int(sys.stdin.readline())
list = []

for i in range(N):
    command = sys.stdin.readline().split()
    if "push" in command:
        list.append(command[1])

    elif "top" in command:
        if len(list)==0:
            print("-1")
        else:
            print(list[-1])
    elif "size" in command :
        print(len(list))
    elif  "empty" in command:
        if len(list) == 0:
            print("1")
        else:
            print("0")
    elif "pop" in command:
        if len(list) == 0:
            print("-1")
        else:
            print(list[-1])
            list.pop()


