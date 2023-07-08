import sys
V = int(sys.stdin.readline())
graph = [[] for i in range(V+1)]
visited = [-1] * (V + 1) # 탐색 여부, 간선의 거리
visited[1] = 0

def dfs(x,y): # x는 노드, y는 누적거리
    for (a, b) in graph[x]:
        if visited[a] == -1:
            visited[a] = b + y
            dfs(a, b+y)

for i in range(V):
    tt = list(map(int, sys.stdin.readline().split()))
    for e in range(1, len(tt)-2, 2):
        graph[tt[0]].append((tt[e],tt[e+1]))

dfs(1,0)
start= visited.index(max(visited))
visited = [-1] * (V + 1)
visited[start] = 0
dfs(start, 0) # 1번 노드부터 가장 먼 노드에서 다시 제일 먼 노드를 찾는다.

# 트리의 지름 출력
print(max(visited))





