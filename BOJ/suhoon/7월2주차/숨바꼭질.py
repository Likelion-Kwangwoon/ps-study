from collections import deque
MAX =10 **5
visited = [0 for i in range(MAX +1)]
N , K = map(int,input().split())

# bfs
def bfs(n, K):
    queue = deque()
    queue.append(n)

    while(queue):
        v =queue.popleft()
        if v == K:
            return visited[v] 
        for next in (v-1, v+1, 2*v):
            if 0 <= next <= MAX and visited[next] == 0:
                visited[next] = visited[v] + 1
                queue.append(next)
         

print(bfs(5,17))
