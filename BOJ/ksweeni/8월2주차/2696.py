from sys import stdin
import heapq

def middlenum(data):
    left, right = [], [] #최대, 최소힙
    middle = data[0]
    result = [middle]
    for idx, val in enumerate(data[1:], 1):
        if val > middle:
            heapq.heappush(right, val) # 중앙값보다 크면 최소힙에 입력
        else:
            heapq.heappush(left, -val) # 작으면 최대 힙에 입력
        if idx % 2 == 0:
            if len(left) < len(right):
                heapq.heappush(left, -middle) # 길이 비교, 더 부족한 쪽에 mid 값을 넣어주고
                middle = heapq.heappop(right) # mid 값 갱신
            elif len(left) > len(right):
                heapq.heappush(right, middle)
                middle = -heapq.heappop(left)
            result.append(middle) # 결정된 middle값을 result 배열에 넣기

    print(len(result))

    for i in range(len(result)):
        if (i + 1) != 1 and (i + 1) % 10 == 1:
            print()
        print(result[i], end=' ')
    print()


t = int(stdin.readline().rstrip())

for _ in range(t):
    m = int(input())
    data = []

    if m % 10 == 0:
        for _ in range(m // 10):
            data.extend(list(map(int, stdin.readline().rstrip().split())))
    else:
        for _ in range(m // 10 + 1):
            data.extend(list(map(int, stdin.readline().rstrip().split())))
    middlenum(data)