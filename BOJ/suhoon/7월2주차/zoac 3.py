SL, SR = input().split()
keyboard = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm']
]
cur = []
for char in SL, SR:
    for i ,row in enumerate(keyboard):
        if char in row:
            cur.append([i+1 , (row.index(char) )+1 ])
            break
word = input()
place = []
for char in word:
    for i ,row in enumerate(keyboard):
        if char in row:
            place.append((i+1 , (row.index(char) )+1 ))
            break

ans = 0

for (a, b) in place:
    if b >= 6 or (a,b)==(3,5):
        ans += abs(cur[1][0]- a) + abs(cur[1][1]-b )
        cur[1] = [a,b]
    else:
        ans += abs(cur[0][0]- a) + abs(cur[0][1]-b )
        cur[0] = [a,b]

print(ans+len(word))
    


