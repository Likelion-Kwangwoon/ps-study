import sys
num = int(sys.stdin.readline())
k = 64
while(num % 2 ==0):
  num//=2
  k-=1
print(k)