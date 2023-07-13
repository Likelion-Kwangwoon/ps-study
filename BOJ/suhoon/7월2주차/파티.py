import sys
import heapq
N , M , X = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))

#print(graph)
INF = int(1e9)
def dijkstra(start):
    distance = [INF] * (N+1)
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while(q):
        dist, now = heapq.heappop(q) #가장 거리가 작은걸 추출
        
        if distance[now] >= dist: #최단 거리가 아니라면
            for (next,weight) in graph[now]: #연결된 노드들 확인
                if dist + weight < distance[next]: #현재 저장되어있는 값보다 작다면
                    distance[next] = dist + weight #업데이트
                    heapq.heappush(q,(distance[next] ,next))

    return distance

ans = 0
for i in range(1, N+1):
    go = dijkstra(i)
    back = dijkstra(X)
    ans = max(ans, go[X] +back[i])

print(ans)
