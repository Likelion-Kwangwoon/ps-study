from itertools import combinations
word = input()
N = len(word)
num = []
result = []
for i in range(1, N):
    num.append(i)
ncr = combinations(num, 2)

for item in ncr:
    a, b =item
    temp_word=list(word[0:a])
    temp_word.reverse()
    temp_word2=list(word[a:b])
    temp_word2.reverse()
    temp_word3=list(word[b:])
    temp_word3.reverse()
    #print(len(temp_word),len(temp_word2),len(temp_word3))
    temp_word.extend(temp_word2)
    temp_word.extend(temp_word3)
    re = "".join(temp_word)
    result.append(re)

print(sorted(result)[0])


