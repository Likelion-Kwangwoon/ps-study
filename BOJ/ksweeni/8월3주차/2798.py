import sys
input = sys.stdin.readline

card, m = map(int, input().split(' '))
li = list(map(int, input().split(' ')))
total = 0

for i in range(card):
  for j in range(i+1,card):
    for k in range(j+1,card):
      if li[i]+li[j]+li[k] <= m:
        total = max(total, li[i]+li[j]+li[k]) # 결국 m에 가까운 최댓값이 정답이 된다
      else:
        continue
        
print(total)