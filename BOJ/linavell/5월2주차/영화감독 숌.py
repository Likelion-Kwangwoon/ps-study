import sys
n = int(sys.stdin.readline())
num = 1
i = 0
while i != n:
    num += 1
    nStr = str(num)
    if "666" in nStr:
        i += 1

print(num)
        