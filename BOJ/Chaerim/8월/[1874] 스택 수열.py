import sys
input = sys.stdin.readline
n = int(input())
st = []
op = []
cnt = 1
flag = True

for i in range(n):
    num = int(input())

    while cnt <= num:
        st.append(cnt)
        op.append("+")
        cnt += 1

    if st[-1] == num:
        st.pop()
        op.append('-')
    else:
        flag = False
        break

print("NO") if not flag else print(*op,sep="\n")