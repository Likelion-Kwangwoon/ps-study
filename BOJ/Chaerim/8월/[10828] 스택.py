import sys
input = sys.stdin.readline

N = int(input())
st = []
for i in range(N):
    t = input().rstrip()
    if t == 'size':
        print(len(st))
    elif t == 'empty':
        if not st: #비었으면
            print(1)
        else:
            print(0)
    elif t == 'top':
        if not st:
            print(-1)
        else:
            print(st[-1])
    elif t == 'pop':
        if not st:
            print(-1)
        else:
            print(st.pop())
    else:
        st.append(t[5:])