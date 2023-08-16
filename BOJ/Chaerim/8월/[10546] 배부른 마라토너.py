import sys
input = sys.stdin.readline
dic1= dict()
N=int(input())

for _ in range(N):
    name = input().rstrip()
    if name in dic1:
        dic1[name] += 1
    else:
        dic1[name] = 1

for _ in range(N-1):
    name_done = input().rstrip()
    dic1[name_done] -= 1

for k,v in dic1.items():
    if dic1[k] != 0:
        print(k)
