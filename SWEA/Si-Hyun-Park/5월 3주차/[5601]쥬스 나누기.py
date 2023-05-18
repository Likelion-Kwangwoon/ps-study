T = int(input())

for t in range(1,T+1):
  n = int(input())
  ans=""
  for i in range(n) :
    ans += f" 1/{n}"
  
  print(f"#{t}{ans}")