import sys
input = sys.stdin.readline

N, M = map(int,input().split())
ball_list = [ i for i in range(1,N+1)] #1,2,3,4,..., N까지의 공
for i in range(M):
    i, j = map(int,input().split())
    ball_list[i-1], ball_list[j-1] = ball_list[j-1], ball_list[i-1]
print(*ball_list)
