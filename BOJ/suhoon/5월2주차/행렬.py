N , M = map(int,input().split())

graph = []
graph2 = []
for i in range(N):
    graph.append(list(map(int,input())))
for i in range(N):
    graph2.append(list(map(int, input())))


if graph == graph2:
    print(0)
    exit()



cnt =0

for i in range(N):
    for j in range(M):
        if graph[i][j] != graph2[i][j]:
            #3x3행렬 바꾸기
            if i+3 >N or j+3 >M: #초과한다면
                continue
            else:
                for k in range(i, i+3):
                    for t in range(j , j+3):
                        if graph[k][t] == 0:
                            graph[k][t] = 1
                        else:
                            graph[k][t] = 0

                cnt +=1
                if graph == graph2:
                    print(cnt)
                    exit()

print(-1)








