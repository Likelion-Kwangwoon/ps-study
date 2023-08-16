import sys
input = sys.stdin.readline

a,b = map(int, input().split(' '))
check = [False] * (b+1)
answer = 0
for i in range(a):
  num = int(input())
  for j in range(num,b+1,num):
    if not check[j]:
      check[j] = True
      answer += 1
print(answer)