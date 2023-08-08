import sys
n = int(sys.stdin.readline())

idx = 0
answer = []

index = [i for i in range(1,n+1)]
li = list(map(int, input().split(' ')))
 
ball = li.pop(idx)
answer.append(index.pop(idx))

while li:
    if ball < 0:  
        idx = (idx + ball) % len(li)
    else:  
        idx = (idx + (ball - 1)) % len(li)
    ball = li.pop(idx)
    answer.append(index.pop(idx))
    
    
for a in answer:
  print(a,end=' ')