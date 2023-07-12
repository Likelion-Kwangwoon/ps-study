import sys
input = sys.stdin.readline
from collections import deque


t = int(input())
#R은 배열 순서를 뒤집고, D는 첫번째 수를 버림
for i in range(t):
    p = input().rstrip()
    n = int(input())
    s = input().rstrip()[1:-1].split(',')
    #비어있는 deque도 길이를 1이라 인식함

    if n == 0:
        q = deque()
    else:
        q = deque(s)

    cnt = 0
    flag = True

    for j in p:
        if j == "R":
            cnt += 1
        else:
            if not q:
                flag = False
                break
            else:
                if cnt % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
    if flag:
        if cnt % 2 == 0:
            print("["+",".join(q)+"]")
        else:
            q.reverse()
            print("["+",".join(q)+"]")
    else:
        print("error")
