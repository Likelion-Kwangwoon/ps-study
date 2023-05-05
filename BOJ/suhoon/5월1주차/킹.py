from copy import deepcopy

a, b ,N = input().split()
N = int(N)
a = list(a)
b = list(b)
a[0] = ord(a[0])-64
b[0] = ord(b[0])-64
a = list(map(int, a))
b = list(map(int, b))
dic = {
    'R' : (1,0),
    'L' : (-1,0),
    'B' : (0,-1),
    'T' : (0,1),
    'RT' : (1,1),
    'LT' : (-1,1),
    'RB' : (1,-1),
    'LB' : (-1,-1)
}

for i in range(N):
    command = input()
    dx,dy = dic[command]
    ax = a[0] + dx
    ay = a[1] + dy

    if 0< ax <= 8 and 0< ay<= 8:
        if ax == b[0] and ay == b[1]:
            bx = b[0] + dx
            by = b[1] + dy
            if 0 < bx <= 8 and 0< by<=8:
                a = [ax,ay]
                b = [bx,by]
        else:
            a = [ax,ay]
    

print(f'{chr(a[0] + 64)}{a[1]}')
print(f'{chr(b[0] + 64)}{b[1]}')                








