import sys
n = int(sys.stdin.readline())
memberList = []
num = 1
for i in range(n):
    a, b = input().split()
    a = int(a)
    memberList.append([a, b, num])
    num += 1
memberList.sort(key = lambda x: (x[0], x[2]))
for i in memberList:
    print(i[0], i[1])