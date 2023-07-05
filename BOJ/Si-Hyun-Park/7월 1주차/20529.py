

def binaryMBTI(m) : 
  e, n, t, j = m
  ans = 0
  if e == "E" : ans += 8 
  if n == "N" : ans += 4
  if t == "T" : ans += 2
  if j == "J" : ans += 1
  return ans

def dist(a, b, c) :
  t = 0
  t += sum(list(map(int, list(str(bin(a^b)[2:])))))
  t += sum(list(map(int, list(str(bin(a^c)[2:])))))
  t += sum(list(map(int, list(str(bin(c^b)[2:])))))
  return t

T = int(input())
for _ in range(T) :
  n = int(input())
  mbti = list(map(binaryMBTI, input().split()))
  ans = 13
  if n > 32 :
    print(0)
    continue
  for i in range(n-2) :
    for j in range(i+1, n-1) :
      for k in range(j+1, n) :
        t = dist(mbti[i],mbti[j],mbti[k])
        if ans > t :
          ans = t
  print(ans)