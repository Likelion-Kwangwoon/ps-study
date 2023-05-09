import sys
n = int(sys.stdin.readline())
wordList = []
onlyWord = []
for i in range(n):
    word = sys.stdin.readline().strip()
    if word not in onlyWord:
        wordList.append([word, len(word)])
        onlyWord.append(word)
    
wordList.sort(key = lambda x: (x[1], x[0]))
for i in wordList:
    print(i[0])