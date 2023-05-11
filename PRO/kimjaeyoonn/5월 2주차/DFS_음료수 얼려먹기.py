'''
얼음틀 N by M
두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어짐.
한 번에 만들 수 있는 아이스크림 개수는?
'''

'''
풀이
1. 특정 지점의 주변 상하좌우를 살펴본다. 값이 0이면서 아직 방문하지 않았다면, 방문 처리
2. 방문한 지점에서 다시 상하좌우 살피면서 반복
3. 방문하지 않은 지점을 count하면 된다.
'''
def dfs(x, y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    
    if graph[x][y] == 0:  # 현재 노드를 아직 방문하지 않았다면,
        graph[x][y] = 1  
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True  # result+=1
    return False

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
print()