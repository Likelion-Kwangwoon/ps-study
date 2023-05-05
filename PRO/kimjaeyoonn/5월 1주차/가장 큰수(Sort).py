'''
0 또는 양의 정수를 이어붙여서 만들 수 있는 가장 큰 수
정렬문제
'''
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)    
    return str(int(''.join(numbers)))