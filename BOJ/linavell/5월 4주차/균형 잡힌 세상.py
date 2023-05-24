import sys
senList = []
sentence = input()
while (sentence != '.'):
    stack = []
    result = True
    # 리스트에 넣기
    senList = list(sentence)
    for i in senList:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                print("no")
                result = False
                break
            if stack.pop() != '(':
                print("no")
                result = False
                break
        elif i == ']':
            if len(stack) == 0:
                print("no")
                result = False
                break
            if stack.pop() != '[':
                print("no")
                result = False
                break
    if result == True:
        if len(stack) == 0:
            print("yes")
        else:
            print("no")
    sentence = input()
        