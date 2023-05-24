import sys
cnt = int(input())
count = list(range(1,cnt+1))
stack=[]
stack_o = []
last=0
cnt_s = 0
if len(count)==1:
    data=int(input())
    if data == 1:
        print("+\n-")
    else:
        print("NO")
    sys.exit()
for i in count:
    data = int(input())
    if data > last:
        while data != count[cnt_s-1]:
            if cnt_s < len(count):
                stack.append(count[cnt_s])
                stack_o.append('+')
                cnt_s+=1
            else:
                print("NO")
                sys.exit()
        if stack:
            stack.pop()
        stack_o.append('-')
    elif data < last:
        if not stack or data != stack.pop():
            print("NO")
            sys.exit()
        else :
            stack_o.append('-')
    last=data
for j in range(len(stack_o)):
    print(stack_o[j])