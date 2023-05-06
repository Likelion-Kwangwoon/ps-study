n = int(input())
room = []
room = [input() for _ in range(n)]

width = 0
height = 0
w_cnt = 0
h_cnt = 0

for i in range (n):
    if w_cnt >= 2 :
            width += 1
            
    if h_cnt >= 2 :
        height += 1
        
    w_cnt = 0
    h_cnt = 0
    
    
    for j in range (n):
        if room[i][j] == '.':
            w_cnt += 1
            
        elif room[i][j] == 'X':
            if w_cnt >= 2 :
                width += 1
            w_cnt = 0
        
        if room[j][i] == '.':
            h_cnt += 1
            
        elif room[j][i] == 'X':
            if h_cnt >= 2 :
                height += 1
            h_cnt = 0 
        
if w_cnt >= 2:
    width += 1

if h_cnt >= 2:
    height += 1


print(width, height)
    