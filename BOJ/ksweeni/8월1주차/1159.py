from string import ascii_lowercase

alpha = {}
for i in ascii_lowercase:
	alpha[i] = 0

for i in range(int(input())):
  name = input()
  alpha[name[0]] +=1

answer = ''
for key, value in alpha.items():
  if value>=5:
    answer+=key

print('PREDAJA') if(answer == '') else print(answer)