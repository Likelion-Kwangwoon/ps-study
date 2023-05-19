T = int(input())
def left(a,b) :
  return a,a+b
def right(a,b) :
  return a+b,b

def euclid(a,b):
  if b > a :
    a, b = b, a
  elif a == b :
    return 1
  while b != 0:
    [a, b] = [b, a%b]
  return a

for t in range(1, T+1) :
  direction = input()
  a,b = 1, 1
  for d in direction :
    if d == "L" :
      a, b = left(a,b)
    elif d == "R" :
      a, b = right(a,b)
  
  gcd = euclid(a,b)
  
  print(f"#{t} {a//gcd} {b//gcd}")
  