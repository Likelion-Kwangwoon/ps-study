import sys

n = int(sys.stdin.readline())
point = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    point.append([a, b])
point.sort(key=lambda x:(x[1], x[0]))
for i in point:
    print(i[0], i[1])