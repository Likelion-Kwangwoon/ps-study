s = list(input())

s_int = list(map(lambda x: ord(x) - 64, s))

print(*s_int, sep=' ')