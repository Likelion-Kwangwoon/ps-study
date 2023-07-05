N = int(input())

tree = {}
ans = []
ans2=[]
ans3=[]

for i in range(N):
    alp = list(input().split())
    tree[alp[0]] = (alp[1],alp[2])
 
def pre(node):
    if node == '.':
        return
    #루트
    ans.append(node)

    #왼쪽
    pre(tree[node][0])

    #오른쪽
    pre(tree[node][1])

def ino(node):
    if node == '.':
        return
    
    #왼쪽
    ino(tree[node][0])

    #루트
    ans2.append(node)

    #오른쪽
    ino(tree[node][1])

def post(node):
    if node == '.':
        return

    #왼쪽
    post(tree[node][0])

    #오른쪽
    post(tree[node][1])

    #루트
    ans3.append(node)

pre('A')
print(''.join(ans))
ino('A')
print(''.join(ans2))
post('A')
print(''.join(ans3))