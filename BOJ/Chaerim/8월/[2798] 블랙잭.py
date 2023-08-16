import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int,input().split())
card = list(map(int,input().split()))
card_3 = list(combinations(card,3))
tot = []
big = 0
flag = False
for i in card_3:
    tot.append(i[0]+i[1]+i[2])

tot = list(set(tot))
tot.sort()

for i in tot:
    if i <= M:
        big = i
    else:
        break
print(big)

