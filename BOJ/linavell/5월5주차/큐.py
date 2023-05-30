import sys

N = int(sys.stdin.readline())
queue = []

for i in range(N):
    inp = sys.stdin.readline().split()

    if inp[0] == "push":
        queue.insert(0, inp[1])

    elif inp[0] == "pop":
        if len(queue) != 0: print(queue.pop())
        else: print(-1)

    elif inp[0] == "size":
        print(len(queue))

    elif inp[0] == "empty":
        if len(queue) == 0: print(1)
        else : print(0)

    elif inp[0] == "front":
        if len(queue) == 0: print(-1)
        else: print(queue[len(queue) -1])

    elif inp[0] == "back":
        if len(queue) == 0: print(-1)
        else: print(queue[0])
        

        