a, b = map(int, input().split())
big = max(a, b)
small = min(a, b)
bigNum = 1
for i in range(1, big+1):
    if a % i == 0:
        if b % i == 0:
            bigNum = i
for i in range(big, a * b + 1):
    if i % a == 0  and i % b == 0:
        smallNum = i
        break

print(bigNum)
print(smallNum)