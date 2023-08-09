from itertools import combinations
import sys
input = sys.stdin.readline
sen = list(input())
st = []
li = []
res = set() # (((1)))에서 발생하는 중복을 제거

for idx, v in enumerate(list(sen)):
    if v == '(':
        st.append(idx)
    elif v == ')':
        li.append([st.pop(), idx])

for i in range(1,len(li)+1):
    combi = combinations(li,i)
    for j in combi:
        tmp = sen
        for k in j:
            start, end = k
            tmp[start] = ''
            tmp[end] = ''
        res.add(''.join(tmp))
    print(res)
for i in sorted(list(res)):
    print(i)
