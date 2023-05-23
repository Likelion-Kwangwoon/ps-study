T = int(input())

for t in range(1, T+1) :
  _ = int(input())
  
  chart = [0 for _ in range(101)]
  student = list(map(int, input().split()))
  
  for s in student :
    chart[s] += 1
  
  ans = 0
  tmp = 0
  for i in range(101) :
    if chart[i] >= tmp :
      ans = i
      tmp = chart[i]
  
  print(f"#{t} {ans}")