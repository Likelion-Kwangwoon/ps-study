N, P ,length = map(int, input().split())

if N != 0:
    numbers = list(map(int, input().split()))
else:
    numbers = []

numbers.append(P)
if len(numbers) > length:
    if numbers[-2] < numbers[-1]:
        numbers.pop(-2)
    else:
        print(-1)
        exit()

numbers.sort(reverse = True)

idx = numbers.index(P)
print(idx+1)
print(numbers)