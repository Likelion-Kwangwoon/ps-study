for _ in range(int(input())):
  n = int(input())
  q1 = set(map(int, input().split())) 
  m = int(input())
  q2 = list(map(int, input().split()))
  for q in q2:
    print(1 if q in q1 else 0)