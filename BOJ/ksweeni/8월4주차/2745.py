import sys
input=sys.stdin.readline

n,b = input().split(' ')
n = n[::-1]

num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = 0
for i, num in enumerate(n):
    answer += int(b) ** i * num_list.index(num)
print(answer)

# 매우 간단 print(int(n,int(b)))