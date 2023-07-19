import sys
from collections import deque
n = int(input())
numList = []
deq = deque(numList)
for i in range(n):
    cmd = sys.stdin.readline()
    cmdList = cmd.split()
    if cmdList[0] == "push_front":
        deq.appendleft(cmdList[1])
    elif cmdList[0] == "push_back":
        deq.append(cmdList[1])
    elif cmdList[0] == "pop_front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif cmdList[0] == "pop_back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif cmdList[0] == "size":
        print(len(deq))
    elif cmdList[0] == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif cmdList[0] == "front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif cmdList[0] == "back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[len(deq)-1])
    
    