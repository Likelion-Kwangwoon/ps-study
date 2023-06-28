N, K = map(int,input().split())
thing = []


for i in range(N):
    W , V = map(int,input().split())
    thing.append([W,V])    

thing.sort(key = lambda x : x[1],reverse = True)
print(thing)



memo = {}
memo[0] = thing[0][1]

# bottom up
for i in range(1,N):



    if thing[i][0] + 
    

print(memo)




