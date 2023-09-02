import sys
input=sys.stdin.readline

poli = input()
poli = poli.replace("XXXX", "AAAA")
poli = poli.replace("XX", "BB")

if 'X' not in poli:
    print(poli)
else:
    print(-1)