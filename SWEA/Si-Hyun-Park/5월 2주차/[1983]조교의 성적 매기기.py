T = int(input())
grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
for t in range(1,T+1) :
  n, k = map(int, input().split())
  
  score = list()
  target = 0
  for i in range(n) :
    mid, end, sub = map(int, input().split())
    
    tmp = mid*0.35 + end*0.45 + sub*0.2
    if i == (k-1) :
      target = tmp
    
    score.append(tmp)
  
  score.sort(reverse=True)
  p = score.index(target)
  
  print("#{} {}".format(t, grade[p//(n//10)]))
    