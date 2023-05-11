T = int(input())
def factorial(n) :
  if (n > 1) :
    return n * factorial(n-1)
  else :
    return 1
def nCr(n) :
  ans = list()
  for i in range(0, n+1) :
    ans.append(factorial(n)//factorial(n-i)//factorial(i))
  
  return ans

for t in range(1, T+1) :
  n = int(input())
  print(f"#{t}")
  for i in range(n) :
    print(*nCr(i))
  