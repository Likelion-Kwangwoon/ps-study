'''
[의상 이름, 의상 종류]로 이루어진 옷장에서
조합을 모두 찾아야 하는데
조건은 하나의 종류에서는 0개 혹은 1개 꺼내는 것임.
2차원 배열로 함수에 들어옴.
'''

def solution(clothes):
    d = {}
    for cloth, type in clothes:
        d[type] = d.get(type, 0)+1  # hash map
        
    answer = 1
    for type in d:
        answer *= (d[type]+1)  # 안입는 경우를 포함해서 몇 종류의 옷을 입을 수 있는지. (조합 계산)
        
    return answer - 1  # 아무것도 입지 않는 경우를 제외함.

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)