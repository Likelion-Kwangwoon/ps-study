n = int(input())
tri = []
for i in range(n):
    tri.append(list(map(int, input().split())))

# bottom up
for i in range(n-1 ,0,-1):
    for j in range(i):
        tri[i-1][j] = max(tri[i][j] ,tri[i][j+1]) + tri[i-1][j]

print(tri[0][0])