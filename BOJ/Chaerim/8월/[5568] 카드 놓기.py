from itertools import permutations
N=int(input())
K=int(input())
li = []
for _ in range(N):
    number = int(input())
    li.append(number)
s1 = set()
per = list(permutations(li,K))
for i in range(len(per)):
    tmp = ""
    for j in range(K):
        tmp += str(per[i][j])
    s1.add(tmp)
print(len(s1))
