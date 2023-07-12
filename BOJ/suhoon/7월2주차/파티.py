import sys
import heapq
N , M , X = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))

print(graph)
INF = int(1e9)
def dijkstra(start):
    distance = [INF] * (N+1)
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while(q):
        dist, now = heapq.heappop(q)
        # 이미 최단거리인지 확인
        if distance[now] < dist:
            continue
        
        for (next,weight) in graph[now]: #연결된 노드들 확인
            if dist + weight < distance[next]: #더 작은 값이 있다면
                distance[next] = dist + weight
                heapq.heappush(q,(distance[next] ,next))

    return distance

ans = 0
for i in range(1, N+1):
    go = dijkstra(i)
    back = dijkstra(X)
    ans = max(ans, go[X] +back[i])

print(ans)
