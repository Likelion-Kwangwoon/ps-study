import sys
import math
t = int(sys.stdin.readline().strip())
for i in range(t):
    lis = []
    n, m = sys.stdin.readline().split()
    n = int(n)
    m = int(m)
    result = math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
    print(result)
    