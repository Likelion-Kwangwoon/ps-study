import sys
n = int(sys.stdin.readline())
start = 1
end = 1
i = 5
num = 1
while n != 1:
    num += 1
    start = end + 1
    end = start + i
    if start <= n and n <= end:
        break
    i += 6

print(num)
