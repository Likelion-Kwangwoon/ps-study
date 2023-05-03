from collections import deque
N = int(input())
graph = []
def BFS(visited, graph, a, b):
    queue = deque()
    queue.append((a,b))
    visited[a][b] = True
    while(queue):
        x, y = queue.popleft()
        

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]


            if nx >= N or ny>=N or nx <0 or ny < 0:
                continue

            if visited[nx][ny] == False and graph[x][y] == graph[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] =True


for i in range(N):
    graph.append(list(input()))

visited = [[False for i in range(N)] for j in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
result1 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] ==False:
            BFS(visited, graph, i, j)
            result1+=1

visited = [[False for i in range(N)] for j in range(N)]
result2 = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            BFS(visited, graph, i , j)
            result2+=1




print(result1,result2)