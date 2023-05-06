import sys
input = sys.stdin.readline
s = input().strip() #공백제거
w = list(input().strip())
st = [] #스택생성
for i in s:
    st.append(i) #스택에 문자하나씩 추가(첫문장 문자열)
    if st[-1] == w[-1] and st[-len(w):] == w: #스택 마지막에 쌓은 단어가 폭탄 마지막 단어와같으면
        for i in range(len(w)):
            st.pop()#삭제
if len(st)==0: #스택 비었으면?
    print("FRULA")
else: #빈게 아니면 문자열 합쳐주자
    print("".join(st))