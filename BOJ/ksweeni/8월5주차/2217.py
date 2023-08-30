import sys
input=sys.stdin.readline

n = int(input())
rope = []

for i in range(n):
  rope.append(int(input()))
rope = reversed(sorted(rope))

res = []

for idx, r in enumerate(rope):
  res.append((idx+1)*r)
print(max(res))