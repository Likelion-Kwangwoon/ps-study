from collections import deque
MAX =10 **5
visited = [-1 for i in range(MAX +1)]
N , K = map(int,input().split())

# bfs
def bfs(n, K):
    queue = deque()
    queue.append(n)
    visited[n] = 0

    while(queue):
        v =queue.popleft()
        print(v)
        if v == K:
            print( visited[v]) 
            return
        for next in (v-1, v+1, 2*v):
            if 0 <= next <= MAX and visited[next] == -1:
    
                visited[next] = visited[v] + 1
                queue.append(next)
         

bfs(N,K)
