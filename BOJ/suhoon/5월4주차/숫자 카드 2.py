import sys
N = int(sys.stdin.readline())
num1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num2 = list(map(int, sys.stdin.readline().split()))
num1.sort()
dic = {}
for item in num1:
    if item not in dic:
        dic[item] =1
    else:
        dic[item] +=1


def binary_search(start, end, target):
    
    while start<= end:  
        mid = (start +end) // 2
        
        if num1[mid] == target:
            return dic[target]

        elif num1[mid]> target:
            end = mid -1 
        else: 
            start = mid+1

    return 0

answer = []
for item in num2:
    answer.append(binary_search(0,len(num1)-1,item))
print(*answer)