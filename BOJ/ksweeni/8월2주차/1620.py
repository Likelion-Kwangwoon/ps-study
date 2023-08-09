import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))

number = {}
name = {}

for i in range(n):
  s = input().rstrip()
  name[i+1] = s
  number[s] = i+1

for i in range(m):
  s = input().rstrip()
  if s.isalpha():
    print(number.get(s))
  else:
    print(name.get(int(s)))