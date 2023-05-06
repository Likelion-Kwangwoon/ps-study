N = int(input())

def factorize(d, num) :
  cnt = 0
  while True :
    if num % d == 0 :
      num //= d
      cnt += 1
    else :
      return [cnt, num]
for n in range(1, N+1) :
  num = int(input())
  
  a, num = factorize(2, num)
  b, num = factorize(3, num)
  c, num = factorize(5, num)
  d, num = factorize(7, num)
  e, num = factorize(11, num)
  
  print("#{} {} {} {} {} {}".format(n, a, b, c, d, e))
  