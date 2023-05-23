def square(a, b) :
  if b > 0 :
    return a * square(a,b-1)
  else :
    return 1
for i in range(1, 11) :
  
  n = int(input())
  a, b = map(int, input().split())
  
  print(f"#{n} {square(a,b)}")