import sys
input = sys.stdin.readline

n = int(input())
fibo = [ 0 for _ in range (n+2)]
fibo[1]=1
for i in range (2, n+2):
  fibo[i] = fibo[i-1] + fibo[i-2]
print(fibo[i-1])