from collections import deque
n = int(input())
deq = deque([ i+1 for i in range(n)])

while(True):
  if len(deq) == 1 :
    break
  deq.popleft()
  deq.append(deq.popleft())
  
print(deq[0])