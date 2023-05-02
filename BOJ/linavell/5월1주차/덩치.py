# 2차원 배열, 1차원 배열 각각 인덱스에 맞게 생성
import sys
i = int(sys.stdin.readline())
info = []
grade = []
for j in range(i):
    h, w = map(int, input().split()) # 키, 몸무게 입력
    info.append([h,w])
    grade.append(1)
for k in range(i):
    for l in range(i):
        if (k != l):
            if (info[k][0] < info[l][0]):
                if (info[k][1] < info[l][1]):
                    grade[k] += 1
                    
for m in grade:
    print(m, end=" ")
