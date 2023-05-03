# 백준 14502번 연구소
from collections import deque
from copy import deepcopy

N, M = map(int, input().split())

graph = []
virus_s = []
for i in range(N):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(M):
        if data[j] == 2:
            virus_s.append([i, j])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

max_safe = 0


def bfs():
    global max_safe
    visited = [[False] * M for _ in range(N)]
    temp = deepcopy(graph)
    for virus in virus_s:
        v_x, v_y = virus
        if visited[v_x][v_y] == True:
            continue
        q = deque()
        q.append([v_x, v_y])
        visited[v_x][v_y] = True

        while q:
            x, y = q.popleft()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                # 범위
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                # 이미 방문
                if visited[nx][ny] == True:
                    continue
                # 벽으로 막혀있음
                if temp[nx][ny] == 1:
                    continue

                if (temp[nx][ny] == 0 or temp[nx][ny] == 2) and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    temp[nx][ny] = 2
                    q.append([nx, ny])

    now_safe = sum(i.count(0) for i in temp)

    max_safe = max(max_safe, now_safe)


def dfs(num):
    if num == 3:
        bfs()
        return

    for x in range(N):
        for y in range(M):
            if graph[x][y] == 0:
                graph[x][y] = 1
                dfs(num + 1)
                graph[x][y] = 0
                # 백트래킹의 가장 중요한 것-->다시 원상태로 돌려주기


dfs(0)
print(max_safe)