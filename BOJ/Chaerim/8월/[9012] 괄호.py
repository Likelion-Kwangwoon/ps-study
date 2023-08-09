import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    st = []
    text = input().rstrip()
    isVPS = True

    for j in text:
        if j == '(':
            st.append(j)
        else:
            if st:
                st.pop()
            else: #짝맞는 괄호가 없을 경우
                isVPS = False
                break
    if not st and isVPS:
        print("YES")
    else:
        print("NO")
