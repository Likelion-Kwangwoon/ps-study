n, m= map(int, input().split())
set1 = set()
set2 = set()
for _ in range(0, n):
    s = input()
    set1.add(s)
for _ in range(0,m):
    s = input()
    set2.add(s)
set3 = set1&set2
setList = list(set3)
setList.sort()
print(len(setList))
for i in setList:
    print(i)
# 1764
