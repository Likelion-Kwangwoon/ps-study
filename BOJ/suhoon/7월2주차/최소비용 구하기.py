import sys
from collections import deque
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))
start , end = map(int, sys.stdin.readline().split())
print(graph)

visited = [-1 for i in range(N+1)]
ans = []
def bfs(start,end):
    queue = deque()
    queue.append(start)
    visited[start]= 0
    while(queue):
        v =queue.popleft()
        print(v)
        if v == end:
            ans.append(visited[v])
            continue
        for (next,dis) in graph[v]:
            if visited[next] == -1:
                queue.append(next)
                visited[next] = visited[v] + dis

bfs(start,end)
print(ans)


#다익스트라