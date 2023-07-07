N ,M  = map(int,input().split())
tru_p = list(map(int,input().split()))
people = set(tru_p[1:])
parties = []
cnt = 0
for i in range(M):
    parties.append(set(map(int, input().split()[1:])))

for i in range(M):
    for party in parties:
        if party & people:
            people = people.union(party)


cnt = 0
for party in parties:
    if party & people:
        continue
    cnt +=1
print(cnt)