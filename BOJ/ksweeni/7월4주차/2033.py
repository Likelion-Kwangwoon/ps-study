n = int(input())
num = 10
while(n > num) :
  diff = n%num
  if diff >= num //2 :
    n += num
  n -= diff
  num*=10
print(n)