import sys


N , M  = map(int,sys.stdin.readline().split())

dic ={}
answer = []
for i in range(N):
    name1 = sys.stdin.readline().rstrip()
    dic[name1] = True

for j in range(M):
    name2 = sys.stdin.readline().rstrip()
    if name2 in dic:
        answer.append(name2)

answer.sort()
print(len(answer))
for item in answer:
    print(item)

