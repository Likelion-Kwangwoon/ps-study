from collections import deque

N = int(input())
people = []
graph = [[] for i in range(N+1)]

for i in range(N):
    people.append(list(input()))



for i in range(N):
    for j in range(N):
        if people[i][j] == 'Y':
            if (j+1) not in graph[i+1]:
                graph[i+1].append(j+1)
            if (i+1) not in graph[j+1]:
                graph[j+1].append(i+1)


result =0 
def BFS(graph,visited, start):
    global result
    count = 0
    queue = deque()
    queue.append((start,0))
    visited[start] = True
    while(queue):
        a, cnt =queue.popleft()
        if cnt >=2:
            continue
        for item in graph[a]:
            if visited[item] ==False :
                queue.append((item,cnt+1))
                visited[item]= True
                count +=1

    result = max(result, count)
            
for i in range(1,N+1):
    visited = [False for i in range(N+1)]
    BFS(graph, visited, i)               
    
print(graph)
print(result)
