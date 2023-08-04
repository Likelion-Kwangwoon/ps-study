import sys
n = int(sys.stdin.readline())
stack = []
for i in range(n):
    command = sys.stdin.readline()
    comList = command.split() #공백 기준으로 나눠서 리스트로 저장
    if comList[0] == "push":
        stack.append(comList[1])
    elif comList[0] == "pop":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])
            stack.pop()
    elif comList[0] == "size":
        print(len(stack))
    elif comList[0] == "empty":
        if len(stack) == 0:
            print("1")
        else:
            print("0")
    elif comList[0] == "top":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])
