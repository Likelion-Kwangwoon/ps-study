import sys
N , M , X = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))

print(graph)


