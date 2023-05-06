from collections import deque
N , K = map(int,input().split())
num = []
result = []

queue = deque()
for i in range(1, N+1):
    queue.append(i)

cnt = 0
while(queue):
    t =queue.popleft()
    cnt += 1
    if cnt == K:
        cnt = 0
        result.append(t)
    else:
        queue.append(t)

print(f'<{", ".join(str(x) for x in result)}>')
