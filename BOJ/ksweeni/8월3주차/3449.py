import sys
input = sys.stdin.readline

for _ in range(int(input())):
  a = input()
  b = input()
  distance = 0
  for i in range(len(a)):
    if a[i] != b[i]:
      distance +=1
      
  print(f"Hamming distance is {distance}.")