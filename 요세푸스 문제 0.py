import sys
input = sys.stdin.readline
from collections import deque

q = deque()
n,k = map(int,input().split())
res = []
for i in range(1,n+1):
    q.append(i)

while q:
    q.rotate(-k)
    res.append(q.pop())

text="<"
for i in range(len(res)):
    if i == len(res)-1:
        text += str(res[i])
    else:
        text+= str(res[i])+", "
text += ">"

print(text)
