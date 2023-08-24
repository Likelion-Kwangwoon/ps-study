# 1,2,3,4,5,... N종류의 아이스크림
# 어떤 종류는 같이 먹으면 형편 없다 웩
N,M = map(int,input().split())
ice = [[False for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    ice[a-1][b-1] = True
    ice[b-1][a-1] = True

result = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if not ice[i][j] and not ice[i][k] and not ice[j][k]:
                result += 1
print(result)