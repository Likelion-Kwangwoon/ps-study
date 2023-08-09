import sys
for _ in range(int(sys.stdin.readline())):
  one = [0]*26
  two = [0]*26
  a=sys.stdin.readline()
  b=sys.stdin.readline()
  for i in range(len(a)-1):
    one[ord(a[i])-97]+=1
      
  for i in range(len(b)-1):
    two[ord(b[i])-97]+=1
  cnt=0
  for i in range(26):
    cnt+= abs(one[i]-two[i])
  print("Case #%d: %d"%(_+1,cnt) )