n= int(input())
s = input()
stack = []
arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)
for j in s:
    if j == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
    elif j == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b-a)
    elif j == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a*b)
    elif j == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b/a)
    else:
        stack.append(arr[ord(j)-65])
print('%.2f' % stack.pop())
