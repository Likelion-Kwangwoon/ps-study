cnt=int(input())
strs = [input() for _ in range(cnt)]
for i in range(len(strs)):
    str = strs[i]
    last=""
    while(str != last):
        last=str
        j=0
        while(1):
            if(j+2>len(str)): break
            elif(str[j]=='(' and str[j+1]==')'): str=str[:j]+str[j+2:]
            else: j=j+1
    if(str==""): print("YES")
    else: print("NO")