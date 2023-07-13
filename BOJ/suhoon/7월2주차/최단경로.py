import sys
import heapq
V , E = map(int,sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[] for i in range(V+1)]

for i in range(E):
    u , v , w = map(int, sys.stdin.readline().split())
    graph[u].append((v , w))

#print(graph)
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (V+1)
    hq = []
    heapq.heappush(hq, (0,start))
    distance[start] = 0
    while(hq):
        dist, now = heapq.heappop(hq) #가장 거리가 작은걸 추출

        if distance[now] >= dist:
            for (next,weight) in graph[now]:
                if distance[next] > dist + weight:
                    distance[next] = dist + weight
                    heapq.heappush(hq,(distance[next], next))

    return distance

for item in dijkstra(K)[1:]:
    if item == int(1e9):
        print("INF")
    else:
        print(item)






