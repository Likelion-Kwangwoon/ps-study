import sys
from collections import defaultdict
from datetime import datetime, timedelta

period_cal = defaultdict() # 기간 계산용 딕셔너리
table = defaultdict(dict) # 대출 기록 딕셔너리

n,l,f = map(str,sys.stdin.readline().split(' '))
n,f,maxperiod = int(n), int(f), timedelta(days=int(l[:3]), hours=int(l[4:6]), minutes=int(l[7:])) # ndays, 00:00:00
minute = timedelta(minutes=1) #00:01:00

for i in range(n):
  line = sys.stdin.readline()
  now = datetime.strptime(line[:16], '%Y-%m-%d %H:%M') #0000-00-00 와 00:00:00으로 변화
  part, name = line[16:].split()
  
  if not period_cal.get(name): # 아무 정보 없으면 등록
    period_cal[name] = 0
    
  if table[name].get(part): #해당 이름과 빌린 부품 기록이 있으면
    period = now - table[name][part] # 기간 계산
    if period > maxperiod: # 기간 초과시 추가 벌금 
      period_cal[name] += ((period - maxperiod) // minute) * f
    del table[name][part] # 대출 기록삭제
    
  else:
    table[name][part] = now #현재 시간으로 대출 등록


res = [(n, f) for n, f in period_cal.items() if f]
if res:
  for name,penalty in sorted(res, key=lambda x: x[0]): # 사전순으로 이름 정렬
    print(name, penalty)
else:
  print(-1)