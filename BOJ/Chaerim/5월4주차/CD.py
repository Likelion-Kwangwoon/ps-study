import sys
while True:
    n,m = map(int, sys.stdin.readline().split())
    if n == 0 and m ==0 :
        break
    set1 = set()
    set2 = set()
    for i in range(n):
        s1 = int(sys.stdin.readline().strip())
        set1.add(s1)
    for i in range(m):
        s2 = int(sys.stdin.readline().strip())
        set2.add(s2)
    print(len(set1&set2))
