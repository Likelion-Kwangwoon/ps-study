T = int(input())

for i in range(1, T + 1):
    num = list(map(int, input().split()))
    ans = 0
    for n in num:
        if n % 2 == 1:
            ans += n
    print("#{} {}".format(i, ans))
