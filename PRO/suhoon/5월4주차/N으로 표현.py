def solution(N, number):
    
    if number == N:
        return 1
    answer = -1
    
    li = [set() for i in range(8)]
    
    for i in range(len(li)):
        li[i].add(int(str(N)*(i+1)))
    
    for i in range(1,8):
        for j in range(i):
            for op1 in li[j]:
                for op2 in li[i-j-1]:
                    li[i].add(op1+op2)
                    li[i].add(op1-op2)
                    li[i].add(op1*op2)
                    if op2 != 0:
                        li[i].add(op1//op2)
        if number in li[i]:
            answer = i +1
            break
        
    #print(li)
    return answer