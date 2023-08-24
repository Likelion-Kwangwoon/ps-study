from itertools import product

N,K = map(int,input().split())
li = list(map(int,input().split()))
length = len(str(N))
li.sort(reverse=True) # 7 5 1
while True:
    num = list(product(li,repeat=length)) #일단 3개씩 중복순열
    for n in num: # 7,7,7 ... 1,1,1 까지 있는 중복순열 집합속에서
        tmp = int(''.join(map(str,n))) # join해서 777부터 이어붙여
        if tmp <= N: # 바로 작은 수가 나오면 출력하고 끝
            print(tmp)
            exit()
    length -= 1 #안나온다면 길이를 줄이자 , 전체 자릿수가 줄어든다.