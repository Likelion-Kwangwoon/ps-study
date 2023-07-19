e, f, c = map(int, input().split())
e+=f
n = (e)//c + (e)%c
answer = (e)//c
while n//c:
    answer += n//c
    n = n//c + n%c
print(answer)