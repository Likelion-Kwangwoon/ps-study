import sys
from collections import defaultdict

word = defaultdict(int)
count = 0 
while True:
    t = str(sys.stdin.readline().rstrip())
    if not t:
        break
    else:
      word[t]+=1
      count += 1 # 나무의 개수 카운트


trees = list(word.keys())
trees.sort() 

for j in trees:
    print("%s %.4f" % (j, word[j] / count * 100))