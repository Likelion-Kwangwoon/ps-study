from collections import deque
import sys
N, M, K, X = map(int, sys.stdin.readline().split())

graph = [[] for i in range(N+1)]
visited = [False for i in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

cnt = [ 0 for i in range(N+1)]
def BFS(start, visited, graph):
 
    queue = deque()
    queue.append(start)
    visited[start] = True
    while(queue):
        node = queue.popleft()
        for item in graph[node]:
            if visited[item] == False:
                queue.append(item)
                visited[item] =True
                cnt[item] += 1
                cnt[item] += cnt[node]
        
BFS(X,visited, graph)

flag = False
for idx, item in enumerate(cnt):
    if idx == 0:
        continue

    if item == K:
        flag = True
        print(idx)

if flag == False:
    print(-1)

