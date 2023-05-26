n, k = map(int, input().split())

person = list(range(1, n + 1))
dead_person = []
index = 0

for i in range(n):
    index += k - 1

    if index >= len(person):
        index %= len(person)

    dead_person.append(person.pop(index))
    
print("<", ", ".join(map(str, dead_person)), ">", sep= "")

#1158
