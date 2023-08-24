A=int(input())
T=int(input())
v=int(input())
li = []
cnt, tot = 0,0
n = 2 #반복 횟수

while cnt != T:
    li += [0,1,0,1]
    for _ in range(n):
        li.append(0)
    for _ in range(n):
        li.append(1)


