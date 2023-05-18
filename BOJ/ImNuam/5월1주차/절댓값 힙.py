import heapq
import sys
heap = []
dic = {}
cnt = int(sys.stdin.readline())
for _ in range(cnt):
    item = int(sys.stdin.readline())
    if item <0:
        heapq.heappush(heap, -item)
        if not -item in dic or dic[-item]==0:
            dic[-item]=1
        else:
            dic[-item]+=1
    elif item>0:
        heapq.heappush(heap,item)
    else:
        if len(heap)>0:
            key = heapq.heappop(heap)
            if not key in dic or dic[key]==0:
                print(key)
            else:
                print(-key)
                dic[key]-=1
        else:
            print(0)
