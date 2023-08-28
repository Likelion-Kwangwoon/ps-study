import sys
input = sys.stdin.readline

a,b,c,m = map(int, input().split(' '))

work, health, hour = 0,0,0

if a > m:
  print(0)
else:
  while(hour!=24):
      hour+=1
      if health+a <= m:
        health+=a
        work+=b
      else:
        if health-c<0:
          health = 0
        else:
          health -= c
  print(work)