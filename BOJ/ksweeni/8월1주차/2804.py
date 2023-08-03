import sys
input = sys.stdin.readline

a, b = input().split()

cross = [['.' for i in range(len(a))] for j in range(len(b))]

index = 0
for i in a:
    if i in b:
        index = i
        break

idx_1 = a.index(index)	# 1
idx_2 = b.index(index)	# 4

for i in range(len(a)):
    cross[idx_2][i] = a[i]
for i in range(len(b)):
    cross[i][idx_1] = b[i]
for c in cross:
    print(''.join(c))