sl, sr = input().rstrip().split(' ')
alpha = input().rstrip()

KEYBOARD = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
MO = 'yuiophjklbnm'
lx, ly, rx, ry = 0,0,0,0
# 첫 위치 구하기 
for i in range(len(KEYBOARD)):
  if sl in KEYBOARD[i]:
    lx , ly = i, KEYBOARD[i].index(sl)
  if sr in KEYBOARD[i]:
    rx, ry = i, KEYBOARD[i].index(sr)

value = 0
for a in alpha:
  value+=1
  if a in MO:
    for i in range(len(KEYBOARD)):
      if a in KEYBOARD[i]:
        cur_rx , cur_ry = i, KEYBOARD[i].index(a)
        value += abs(rx-cur_rx)+abs(ry-cur_ry)
        rx , ry = cur_rx , cur_ry
        break
  else:
    for i in range(len(KEYBOARD)):
      if a in KEYBOARD[i]:
        cur_lx , cur_ly = i, KEYBOARD[i].index(a)
        value += abs(lx-cur_lx)+abs(ly-cur_ly)
        lx , ly = cur_lx , cur_ly
        break

print(value)