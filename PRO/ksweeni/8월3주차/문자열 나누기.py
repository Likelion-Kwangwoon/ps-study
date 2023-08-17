def solution(s):
    answer = 0
    first = 0
    another = 0
    for i in s:
        if first == another:
            answer += 1
            x = i
        if i == x:
            first += 1
        else:
            another += 1            
    return answer