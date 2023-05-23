import sys

n=sys.stdin.readline()
a=list(sys.stdin.readline().split())
b=list(sys.stdin.readline().split())
m=int(sys.stdin.readline().strip())
c=list(sys.stdin.readline().split())


for i in range(len(a))[::-1]:
    if a[i]=='1':
        del b[i]

if len(b) == 0:
    print(*c)
    exit()

b.reverse()
res = ' '.join(b)
print(res)
res += ' '
res += ' '.join(c)
print(len(res))
print(res[:2*m-1])