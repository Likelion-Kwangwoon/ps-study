import sys
import heapq
input = sys.stdin.readline
INF = int(1e9) #무한을 의미하는 값으로 10억 설정

n,m=map(int, input().split()) # 노드 개수, 간선 개수 
start = int(input()) #시작 노드 번호

# 각 노드에 연결되어있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]


# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
  a,b,c = map(int, input().split())
  # a번 노드에서 b번 노드로 가는 비용이 c
  graph[a].append((b,c))


def dijkstra(start):
  # 시작 노드에 대한 초기화
  q = [] # 시작 노드로 가기 위한 최단 경로는 0, 큐에 삽입
  heapq.heappush(q,(0,start))
  distance[start]=0
  while q: #큐가 비어있지 않다면
    dist, now = heapq.heappop(q) # 가장 최단거리가 짧은 노드 꺼내기
    # 현재 노드가 이미 처리된 적 있으면 무시
    if distance[now] < dist:
      continue
    
  # 현재 노드와 연결된 다른 인접한 노드들 확인
    for i in graph[now]:
      cost = dist + i[1]
      # 현재 노드 거쳐 다른 노드로 이동하는 거리가 더 짧으면 갱신
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))
   
  
dijkstra(start) # 다익스트라 알고리즘 수행
for i in range(1,n+1): # 모든 노드로 가기 위한 최단거리 출력
  if distance[i] == INF:
    print("INF")
  else: # 도달할 수 있으면 거리 출력 
    print(distance[i])