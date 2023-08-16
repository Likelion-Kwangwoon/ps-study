import sys
input = sys.stdin.readline

dic = {}
res = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    if tree in dic:
        dic[tree] += 1
    else:
        dic[tree] = 1
    res += 1

dic = sorted(dic.items(), key=lambda x:x[0])
for i,j in dic:
    print('{} {:.4f}' .format(i, (j/res)*100))