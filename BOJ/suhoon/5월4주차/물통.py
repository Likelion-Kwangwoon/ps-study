from collections import deque
A,  B, C = map(int, input().split())
visited = []
answer = []


def BFS(C, visited):

    queue =deque()
    queue.append((0,0,C))


    while(queue):
        x, y ,z = queue.popleft()

        if (x,y) in visited:
            continue
        if x == 0:
            answer.append(z)

        visited.append((x,y))
          # A->B
        if x+y > B: # a->b로 옮기는데 b에서 넘쳐남
            queue.append((x+y-B,B,z))
        else: # a->b로 옮기는데 b를 다 못채움
            queue.append((0,x+y,z))
        
        # A->C
        if x+z > C: # A->C로 옮기는데 C에서 넘쳐남
            queue.append((x+z-C,y,C))
        else: # A->C로 옮기는데 C를 다 못채움
            queue.append((0,y,x+z))

        # B->C    
        if y+z > C: # B->C로 옮기는데 C에서 넘쳐남
            queue.append((x,y+z-C,C))
        else: # B->C로 옮기는데 C를 다 못채움
            queue.append((x,0,y+z))

        # B->A
        if y+x > A: # B->A로 옮기는데 A에서 넘쳐남
            queue.append((A,y+x-A,z))
        else: # B->A로 옮기는데 A를 다 못채움
            queue.append((y+x,0,z))

        # C->A
        if z+x > A: # C->A로 옮기는데 A에서 넘쳐남
            queue.append((A,y,z+x-A))
        else: # C->A로 옮기는데 A를 다 못채움
            queue.append((x+z,y,0))

        # C->B
        if z+y > B: # C->B로 옮기는데 B에서 넘쳐남
            queue.append((x,B,z+y-B))
        else: # C->B로 옮기는데 B를 다 못채움
            queue.append((x,z+y,0))
        
       
    


BFS(C, visited)
answer.sort()
print(*answer)
