from collections import deque
import sys

cnt = int(input())

for i in range(cnt):
    length, where = map(int, sys.stdin.readline().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    count = 0
    while queue:
        best = max(queue)
        front = queue.popleft()
        where-=1
        
        if best == front:
            count+=1
            if where <0:
                print(count)
                break
            
        else:
            queue.append(front)
            if where<0:
                where = len(queue) - 1