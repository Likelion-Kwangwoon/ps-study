n, m = map(int, input().split())
picture = [[0 for col in range(101)] for row in range(101)]

paper = []
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            picture[i][j] += 1
            
num = 0
for i in picture:
    for j in i:
        if (j > m):
            num += 1
            
print(num)