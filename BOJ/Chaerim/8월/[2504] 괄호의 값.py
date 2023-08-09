import sys
input = sys.stdin.readline
str= list(input().rstrip())
st = []
tmp = 1
res = 0
flag = True

for i in range(len(str)):

    if str[i] == '[':
        st.append(str[i])
        tmp *= 3

    elif str[i] == '(':
        st.append(str[i])
        tmp *= 2

    elif str[i] == ']':
        if not st or st[-1] != '[':
            flag = False
            break

        if str[i-1] == '['  : #짝맞음
            res += tmp
        st.pop()
        tmp //= 3

    elif str[i] == ')':
        if not st or st[-1] != '(': #짝 안맞음
            flag = False
            break

        if str[i-1] == '(':
            res += tmp
        st.pop()
        tmp //= 2 #tmp 초기화

print(0) if not flag or st else print(res)
