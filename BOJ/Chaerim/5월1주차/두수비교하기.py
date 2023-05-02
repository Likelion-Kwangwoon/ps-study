# input()함수보다 sys를 쓰는 것이 속도가 더 빠르다.
import sys
input = sys.stdin.readline
A,B = map(int,input().split())
print('==') if A==B else print('>') if A>B else print('<')