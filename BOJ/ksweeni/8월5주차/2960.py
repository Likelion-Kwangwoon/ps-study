import sys
input=sys.stdin.readline

n,k = map(int, input().split(' '))
number = [ True for i in range(n+1)]
count = 0
for i in range(2,n+1):
  for j in range(i,n+1,i): # 배수들만 확인
    if number[j]:
      number[j]=False
      count+=1
      if count == k:
        print(j)
        break