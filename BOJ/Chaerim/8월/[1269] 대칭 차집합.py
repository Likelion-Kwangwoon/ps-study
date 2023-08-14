import sys
input = sys.stdin.readline

A,B = map(int,input().split())
setA = set(map(int,input().split()))
setB = set(map(int,input().split()))

n1 = len(setA-setB)
n2 = len(setB-setA)
print(n1+n2)