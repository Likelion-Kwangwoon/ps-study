import sys
input = sys.stdin.readline


N = int(input())
s = input().rstrip()
st = []
num_list = [0]*N
for i in range(N):
    num_list[i] = int(input())

for i in s:
    if 'A' <= i <= 'Z': #변환되면 숫자이면 스택에 넣기기
        st.append(num_list[ord(i)-65]) #만약에 문자가 C이면 인덱스 2에 들어가고 이런식
    else: #숫자나 연산자일때
        str1 = st.pop() #뒤에값
        str2 = st.pop()

        if i == '+':
            st.append(str1+str2)
        elif i == '-':
            st.append(str2-str1)
        elif i == '*':
            st.append(str2*str1)
        elif i == '/':
            st.append(str2/str1)

print('%.2f' %st[0])