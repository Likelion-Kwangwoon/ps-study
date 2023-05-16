from collections import deque
n = int(input())
deq= deque()
deq.append(n)
a = n

while len(deq) < n:
    deq.appendleft(a-1)
    deq.rotate(a-1)
    a -= 1

for _ in range(len(deq)):
    print(deq.popleft(), end=" ")
