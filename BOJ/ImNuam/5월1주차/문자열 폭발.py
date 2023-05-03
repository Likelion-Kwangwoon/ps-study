string = input()
word = input()
size_s=len(string)
size_w=len(word)
for i in range(size_s-size_w+1):
    for j in range(size_w):
        if(size_s-i-j-1<len(string)):    
            if(string[size_s-i-1-j]!=word[size_w-j-1]):
                break
        else:
            break
        if(j==size_w-1):
            string=string[:size_s-i-size_w]+string[size_s-i:]
    if(string==''):
        print("FRULA")
        break
print(string)