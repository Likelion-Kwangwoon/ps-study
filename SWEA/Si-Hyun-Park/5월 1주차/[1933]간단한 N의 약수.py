N = int(input())

d = list()

for i in range(1, int(N**(1/2)) + 1) :
  if (N % i == 0) :
    d.append(i)
    if((i**2) != N) :
      d.append(N // i)
d.sort()

print(*d, sep=' ')