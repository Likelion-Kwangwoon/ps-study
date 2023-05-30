from copy import deepcopy
from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

answer = 0 
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

virus = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus.append( (i,j) )


def BFS():
    queue = deque()
    temp_graph = deepcopy(graph)

    for item in virus:
        a, b = item
        queue.append((a,b))
   



    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or ny >= M or nx < 0 or ny < 0:
                continue
            if temp_graph[nx][ny] == 0:
                temp_graph[nx][ny] = 2
                queue.append((nx, ny))
                

    global answer
    cnt = 0
    for i in range(N):
        cnt += temp_graph[i].count(0)
    answer = max(answer, cnt)


def makeWall(cnt):
 
    if cnt == 3:
        BFS()
        return
    

    else:

        for i in range(N):
            for j in range(M):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    makeWall(cnt+1)
                    graph[i][j] = 0


makeWall(0)
print(answer)
