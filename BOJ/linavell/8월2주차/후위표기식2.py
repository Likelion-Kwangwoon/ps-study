import string
n = int(input())
strn = list(input())
alpha = []
for i in range(n):
    alpha.append(int(input())) 
stack=[]
for s in strn:
    if s.isalpha():
        stack.append(alpha[ord(s) - ord('A')]) # 아스키코드 숫자로 변환하는 함수 ord()
    else:
        n2 = stack.pop()
        n1 = stack.pop()
        if s == '+' :
            stack.append(n1+n2)
        elif s == '-':
            stack.append(n1-n2)
        elif s == '*':
            stack.append(n1*n2)
        elif s == '/':
            stack.append(n1/n2)
print(format(stack[0], ".2f")) # 소수점 표기