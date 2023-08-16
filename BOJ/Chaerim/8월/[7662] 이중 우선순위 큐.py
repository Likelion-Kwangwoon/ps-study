import sys, heapq
input = sys.stdin.readline

T=int(input())
for i in range(T):
    k = int(input())
    hq = []

    for j in range(k):
        word, n = input().split()
        n = int(n)
        if word == "I":
            heapq.heappush(hq, n)
        else:
            if not hq:
                continue
            if n == 1:
                max_value = max(hq)
                hq.remove(max_value)
            elif n == -1:
                heapq.heappop(hq)

    if not hq:
        print("EMPTY")
    else:
        print(max(hq), hq[0])
