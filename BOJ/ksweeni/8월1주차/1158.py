import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())
people = deque([i for i in range(1,n+1)])
print("<", end='')
while True :
    for _ in range(k-1) :
        people.append(people.popleft())
    print(people.popleft(), end='')
    if people: 
        print(', ', end='')
    else :
        break
print('>')