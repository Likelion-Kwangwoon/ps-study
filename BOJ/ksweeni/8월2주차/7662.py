import heapq
import sys
input = sys.stdin.readline

for t in range(int(sys.stdin.readline())):
  k = int(sys.stdin.readline())
  visited = [False] * k # 방문 여부 체크 배열 
  max_hq = []
  min_hq = []
  
  for i in range(k):
    op, num = sys.stdin.readline().split()
    if op == 'I':
      heapq.heappush(min_hq,(int(num),i)) # 최소힙에는 원본과 튜플 순서 입력
      heapq.heappush(max_hq,(-int(num),i)) # 최대힙에는 음수와 튜플 순서 입력
      visited[i] = True # 방문 처리
      
    elif op == 'D' and int(num) == 1: # 최댓값 삭제
      while max_hq and not visited[max_hq[0][1]]: # 방문 순서가 true일때까지
        heapq.heappop(max_hq) # pop시켜 없앤다
      if max_hq: # 방문 순서가 true인 걸 찾으면
        visited[max_hq[0][1]] = False # False 처리, 최댓값을 pop시킨다
        heapq.heappop(max_hq)
        
    elif op == 'D' and int(num) == -1: # 최솟값 삭제
      while min_hq and not visited[min_hq[0][1]]:
        heapq.heappop(min_hq)
      if min_hq:
        visited[min_hq[0][1]] = False
        heapq.heappop(min_hq)
        
  while min_hq and not visited[min_hq[0][1]]: # 아직 남아있는 것들 또한 제거시켜준다
    heapq.heappop(min_hq)
  while max_hq and not visited[max_hq[0][1]]:
    heapq.heappop(max_hq)
  print(-max_hq[0][0], min_hq[0][0]) if max_hq and min_hq else print("EMPTY")