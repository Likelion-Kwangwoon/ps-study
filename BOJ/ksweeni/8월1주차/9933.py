n = int(input())
str = [input().rstrip() for i in range(n)]

for i in range(n):
    for j in range(i,n):
        if str[i][::-1] == str[j]:
          print(len(str[i]), str[i][len(str[i])//2])
          exit()