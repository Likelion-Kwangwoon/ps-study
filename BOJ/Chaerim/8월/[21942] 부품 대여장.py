import sys
from collections import defaultdict
from datetime import datetime
input = sys.stdin.readline

# 분 변환
def changeMinute(l):
    day,text = l.split('/')
    day = int(day)
    hour, minute = map(int,text.split(':'))
    total_minute = minute + hour*60 + day*24*60
    return total_minute

#명수, 대여기간, 벌금 파싱
N, L, F = input().split()
N = int(N)
F = int(F) #벌금
tot_min = changeMinute(L) #총 기간을 분수 변환 완료!

rent_dic = defaultdict(dict) #빌린 명부
fine_dic = defaultdict(int) #벌금 명부

for _ in range(N):
    sentence = input()
    now = datetime.strptime(sentence[:16],'%Y-%m-%d %H:%M')
    part, name = sentence[16:].split()
    #분리 끝냄

    if rent_dic[name].get(part):
        borrow = now - rent_dic[name][part]
        rent_time = borrow.days*60*24 + borrow.seconds//60
        if rent_time > tot_min:
            fine_dic[name] += (rent_time-tot_min)*F
        del rent_dic[name][part]
    else: #빌려간 명부에 없으면 추가
        rent_dic[name][part] = now

if len(fine_dic.keys()): #벌금 명부 비어있지 않은 경우
    fine_list = sorted(fine_dic.keys()) #사람 순으로 정렬
    for person in fine_list:
        print(person,int(fine_dic[person]))
else:
    print(-1)