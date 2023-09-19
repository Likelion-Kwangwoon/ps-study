import sys
n = int(input())
stack = []

people = [2,4,1,2,2,5,1]
count = 0
HEIGHT, CNT = 0 , 1


# (키, 사람 수)
for p in people:
  while stack and stack[-1][HEIGHT] <= p:
    count+=stack.pop()[CNT] # 사람 수 저장
    
  if not stack: # 없으면 일단 저장
    stack.append((p,1))
    continue
    
  if stack[-1][HEIGHT] == p: # 키가 같은 사람이면 일단 그 수 저장 
    cnt = stack.pop()[CNT]
    count+=cnt
    
    if stack: # 내부에 사람들이 더 있는거면 같은 키로 더 볼 수 있는 인원이 있다는 뜻
      count+=1
      stack.append((p,cnt+1)) # 같은 키 인원 갱신
      
  else: # 스택 내부에 나보다 큰 사람이 있다는 것, 1명만 볼 수 있다
    stack.append((p,1))
    count+=1

print(count)