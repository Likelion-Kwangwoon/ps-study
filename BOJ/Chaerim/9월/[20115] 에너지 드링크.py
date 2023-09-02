N=int(input())
drink = list(map(int,input().split()))

max_value = max(drink)
res = max_value

for i in drink:
    if i == max_value:
        pass
    else:
        res += i/2

print('%.5f'%res)