import sys
n = int(sys.stdin.readline())
numList = []
for i in range(n):
    numList.append(int(sys.stdin.readline()))
numSet = set(numList)
numList = list(numSet)
numList.sort()
for i in numList:
    print(i)
