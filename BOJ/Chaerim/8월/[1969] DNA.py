N,M=map(int,input().split())
res = []

for _ in range(N):
    res.append(list(map(str,input())))
cnt, tot = 0,0
result=''

for i in range(M):
    a,c,g,t = 0,0,0,0
    for j in range(N):
        if res[j][i] == 'T':
            t += 1
        elif res[j][i] == 'A':
            a += 1
        elif res[j][i] == 'G':
            g += 1
        elif res[j][i] == 'C':
            c += 1
    if max(a,c,g,t) == a: #사전순 시작
        result += 'A'
        tot += c+g+t
    elif max(a,c,g,t) == c:
        result += 'C'
        tot += a+g+t
    elif max(a,c,g,t) == g:
        result += 'G'
        tot += a+c+t
    else:
        result += 'T'
        tot += a+c+g
print(result)
print(tot)
