from queue import PriorityQueue
que = PriorityQueue()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
present = True

for i in arr:
    que.put(-i) #내림차순으로 선물 정렬해서 넣음

for i in range(m):
    num = -(que.get())
    if arr2[i] <= num:
        que.put(arr2[i] - num)
    else:
        present = False
        break
print(1 if present == True else 0)


# 23757 Data structure