
N = int(input())
nos = list(map(int,input().split()))
answer = [0 for i in range(N)]
answer[nos[0]] = 1
for i in range(1, N):
    cnt =nos[i]+1
    cur = 0
    while(cnt):
        if answer[cur] ==0 :
            cnt -=1
        cur +=1
    answer[cur-1] = i +1

print(*answer)


































