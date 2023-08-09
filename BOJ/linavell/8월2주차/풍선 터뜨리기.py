from collections import deque
d = deque()
N = int(input())
dList = list(map(int, input().split()))
idx = 1
for i in dList:
    d.append([i, idx])
    idx += 1

print(1, end=" ")

num = d.popleft() # 1번 풍선 터뜨리기
while len(d) != 0:
    
    if num[0] > 0:
        for i in range(num[0]-1):
            d.append(d.popleft())
        num = d.popleft() # 다음 풍선 터뜨리기
        
        print(num[1], end=" ")
    else:
        for i in range(-(num[0]) - 1):
            d.appendleft(d.pop())
        num = d.pop()
        print(num[1], end=" ")

