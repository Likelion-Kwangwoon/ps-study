T = int(input())

for t in range(1, T+1) :
  a, b = map(int, input().split())
  
  print(f"#{t} {(a+b)%24}")