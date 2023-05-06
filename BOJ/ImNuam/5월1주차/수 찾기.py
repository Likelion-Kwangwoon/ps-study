cnt_A = int(input())
arr_A=list(map(int, input().split()))
cnt_B=int(input())
arr_B=list(map(int, input().split()))
arr_A.sort()
for i in range(cnt_B):
    s=0
    e=cnt_A-1
    while(1):
        m=(s+e)//2
        if(arr_B[i]<arr_A[m]):
            e=m-1
        elif(arr_B[i]>arr_A[m]):
            s=m+1
        elif(arr_B[i]==arr_A[m]):
            print(1)
            break
        if(s>e):
            print(0)
            break
        
