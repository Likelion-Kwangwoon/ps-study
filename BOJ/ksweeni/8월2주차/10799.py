str = list(input())
count = 0
stack = []

for i in range(len(str)):
    if str[i] == '(':
        stack.append('(')

    else:
        if str[i-1] == '(': 
            stack.pop()
            count += len(stack)

        else:
            stack.pop() 
            count += 1 

print(count)