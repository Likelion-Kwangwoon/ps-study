X = int(input())


i =0
cnt = 0
while(1):
    i +=1
    if (X - i) > 0:
        X -= i
        cnt += 1
    else:
        break
    

#print(X, cnt)

if (cnt+1) %2 ==0:# 짝수번째 줄이면 밑으로 내려가고
    print(str(X) + "/" +str( cnt +1 - X +1 ))


else:#홀수번쨰 줄이면 위로올라감
     print(str(cnt +1 - X +1)+ "/" + str(X))









