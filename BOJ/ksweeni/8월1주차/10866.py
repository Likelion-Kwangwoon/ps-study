from collections import deque
import sys

n = int(input())
deq = deque()

for i in range(n):
  op = sys.stdin.readline().rstrip().split()

  if 'push_front' in op[0]:
    deq.appendleft(op[1])
  elif 'push_back' in op[0]:
    deq.append(op[1])
  elif 'pop_front' in op[0]:
    print(deq.popleft()) if deq else print(-1)
  elif 'pop_back' in op[0]:
    print(deq.pop()) if deq else print(-1)
  elif 'size' in op[0]:
    print(len(deq))
  elif 'empty' in op[0]:
    print(0) if deq else print(1) 
  elif 'front' in op[0] :
    print(deq[0]) if deq else print(-1) 
  elif 'back' in op[0]:
    print(deq[-1]) if deq else print(-1)