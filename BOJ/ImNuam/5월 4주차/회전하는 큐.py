import sys
class que:
    def __init__(self, length):
        self.arr = [n+1 for n in range(length)]
        self.idx=0
inp = sys.stdin.readline().split()
leng,cnt = int(inp[0]), int(inp[1])
q=que(leng)
res=0
where=0
get=sys.stdin.readline().split()
for i in range(cnt):
    what = int(get[i])
    for  n in range(len(q.arr)):
        if q.arr[n]==what:
            where = n
            break
    if (where-q.idx+len(q.arr))%len(q.arr)<=(len(q.arr)-where+q.idx+len(q.arr))%len(q.arr):
        res+=(where-q.idx+len(q.arr))%len(q.arr)
        del q.arr[where]
        q.idx=where
    else:
        res+=(len(q.arr)-where+q.idx+len(q.arr))%len(q.arr)
        del q.arr[where]
        q.idx=where
print(res)