import sys
input = sys.stdin.readline

a, b = map(str, input().split(' '))

minnum = int(a.replace('6','5'))+int(b.replace('6','5'))
maxnum = int(a.replace('5','6'))+int(b.replace('5','6'))

print(minnum, maxnum)