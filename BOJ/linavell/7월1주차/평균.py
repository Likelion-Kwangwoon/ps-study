N = int(input())
scoreList = list(map(int, input().split()))
bigScore = max(scoreList)
for i in scoreList:
    scoreList[scoreList.index(i)] = i/bigScore*100
average = sum(scoreList) / len(scoreList)
print(average)