N=int(input())
color = list(input().rstrip())
cnt = 1

colors = {'B':0, 'R':0}
colors[color[0]] += 1
for i in range(1,N):
    if color[i] != color[i-1]: #전과 다를때만 칠한다
        colors[color[i]] += 1

cnt += min(colors['B'], colors['R'])
print(cnt)