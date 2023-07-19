n, k = map(int, input().split())
li = list(map(int, input().split()))
answer = []

for i in range(0, n-k+1):
    answer.append(sum(li[i:i+k]))
    
print(max(answer))