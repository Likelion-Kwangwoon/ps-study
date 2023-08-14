import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N=int(input())
    li = list(map(int,input().split()))
    M=int(input())
    li2 = list(map(int,input().split()))
    set1 = set(li)
    for i in li2:
        if i in set1:
            print(1)
        else:
            print(0)