from collections import deque
n, k = map(int, input().split())

cirq = deque([i for i in range(1,n+1)])

ans = list()
i = 1
while cirq :
  if i % k == 0 :
    ans.append(cirq.popleft())
  else :
    cirq.append(cirq.popleft())
  i += 1

print("<", end ="")
print(*ans, sep=", ", end="")
print(">")