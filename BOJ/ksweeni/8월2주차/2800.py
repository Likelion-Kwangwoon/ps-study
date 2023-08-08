from itertools import combinations

str = list(input()) 
p, pair_idx = [],[] # 괄호쌍 찾을 스택 -> p , 괄호쌍 인덱스 저장 이중리스트 ->pair_idx
answer=set() # 중복 제거한 결과 집합

for i,v in enumerate(str): 
    if v == '(':
        str[i]=''
        p.append(i)
    if v == ')':
        str[i]=''
        pair_idx.append([p.pop(),i])    # 괄호의 [start,end] 쌍이 저장된 pair_idx


for i in range(len(pair_idx)): ## 괄호쌍의 조합(combinations)을 이용해 괄호 추가
    for j in combinations(pair_idx,i):
        P=str[:] 
        for s,e in j:
            P[s]='(';P[e]=')' 
        answer.add(''.join(P))
      
print(*sorted(answer),sep='\n') 