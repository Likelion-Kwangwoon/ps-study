s = input()
cnt = 0
stack = []
for i in range(len(s)):
    if s[i] == ')':
        if s[i-1] == ')':
            stack.pop()
            cnt += 1
        else:
            stack.pop()
            cnt += len(stack)
    else:
        stack.append(i)
print(cnt)

#10799 쇠막대기 Data stucture