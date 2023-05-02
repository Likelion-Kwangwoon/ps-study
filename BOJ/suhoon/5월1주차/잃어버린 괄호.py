import re

word = input()
flag = False

for idx, item in enumerate(word):
    if item == '-':
        word1 = word[0:idx]
        word2 = word[idx:]
        flag = True
        break

if flag == False:
    word_split = word.split('+')
    word_split = list(map(int, word_split))
    print(sum(word_split))

else:
    word1_split = word1.split('+')
    word2_split = re.split('\+|\-', word2)

    word1_split = list(map(int, word1_split))
    word2_split = list(map(int, word2_split[1:]))
    print(sum(word1_split)-sum(word2_split))
