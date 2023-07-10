from collections import deque
MAX =10 **5
visited = [-1 for i in range(MAX +1)]
N , K = map(int,input().split())

result = 0
#bfs
def bfs(n, K):
    global result
    queue = deque()
    queue.append(n)
    visited[n] = 0

    while(queue):
        v =queue.popleft()
        if v == K:
            result +=1
            continue
            #(continue , 없음) (밑에 조건식 때문에)
            
        for next in (2*v, v+1, v-1):
            if 0 <= next <= MAX:
                # 첫방문 혹은 방문 시간이 같은 경우가 이미 있음(가장 빠른 시간 방법의 수를 위해)
                if(visited[next] == -1 or visited[next] == visited[v] + 1):
                    visited[next] = visited[v] + 1
                    queue.append(next)
bfs(N,K)
print(visited[K])
print(result)





