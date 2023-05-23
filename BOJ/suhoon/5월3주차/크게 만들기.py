N , K = map(int,input().split())

num = input()
num = list(map(int,num))
cnt = K
while(cnt != 0):
    temp_num = num[0:N-K]
    t = min(temp_num)
    tt = num.index(t)
    num.pop(tt)
    cnt -=1

print(''.join(map(str, num)))    

