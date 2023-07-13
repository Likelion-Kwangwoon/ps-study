import sys
input = sys.stdin.readline
 
dic = {}
answer = 0
 
for i in range(int(input())):
    a,b = map(int, input().split())
    if a not in dic:
        dic[a] = b
    else:
        if dic[a] != b:
            answer +=1
            dic[a] = b
 
print(answer)