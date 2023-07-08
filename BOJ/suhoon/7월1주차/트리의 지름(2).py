import sys
from collections import deque
V = int(sys.stdin.readline())
graph = [[] for i in range(V+1)]
visited = [-1] * (V + 1) # 탐색 여부, 간선의 거리
def bfs(node):
    queue = deque()
    queue.append(node)
    visited[node] = 0
    while(queue):
        n =queue.popleft()
        for item in graph[n]:
            a,b = item
            if visited[a] == -1:
                queue.append(a)
                visited[a] = visited[n] + b


for i in range(V):
    tt = list(map(int, sys.stdin.readline().split()))
    for e in range(1, len(tt)-2, 2):
        graph[tt[0]].append((tt[e],tt[e+1]))


bfs(1)

start= visited.index(max(visited))
visited = [-1] * (V + 1) # 탐색 여부, 간선의 거리
bfs(start)
# 트리의 지름 출력
print(max(visited))