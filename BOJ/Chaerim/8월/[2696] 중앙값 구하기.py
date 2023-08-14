import sys, heapq
input = sys.stdin.readline

def fn(arr2):
    left, right = [], []
    middle = arr2[0]
    res_arr = [middle]
    for idx, n in enumerate(arr2[1:], start=1): #0번째 원소는 이미 넣었으니까 패스
        if n > middle:
            heapq.heappush(right, n)
        else:
            heapq.heappush(left, -n)

        if idx % 2 == 0: #홀수번째 수 일때
            if len(left) < len(right):
                heapq.heappush(left, -middle)
                middle = heapq.heappop(right)
            elif len(left) > len(right):
                heapq.heappush(right, middle)
                middle = -heapq.heappop(left)
            res_arr.append(middle)
    length = len(res_arr)
    print(length)

    for j in range(length):
        if length > 10:
            if j != 0 and j % 10 == 0:
                print()
        print(res_arr[j],end=' ')
    print()

T=int(input())
for _ in range(T):
    M = int(input())
    li = []
    if M < 10: #배열 길이가 10 밑에 일때
        li.extend(list(map(int, input().rstrip().split())))
    else: # 배열 길이가 10 이상이면 li 리스트에 계속 덧붙인다.
        for _ in range(M//10 + 1):
            li.extend(list(map(int,input().rstrip().split())))
    fn(li)