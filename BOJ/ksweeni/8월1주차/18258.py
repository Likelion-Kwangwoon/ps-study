from collections import deque
import sys
input = sys.stdin.readline
queue = deque()

for i in range(int(input())):
  op = input()
  if 'push' in op:
    o,n = op.split(' ')
    queue.append(int(n))
  elif 'pop' in op:
    print(queue.popleft()) if queue else print(-1)
  elif 'front' in op:
    print(queue[0]) if queue else print(-1)
  elif 'back' in op:
    print(queue[-1]) if queue else print(-1)
  elif 'size' in op:
    print(len(queue))
  elif 'empty'in op:
    print(0) if queue else print(1)