'''
1. 어떤 장르르 먼저 틀까?
2. 장르 내에서 상위 2개 선정
'''
def solution(genres, plays):
    answer = []    
    
    d = {}
    for g, p in zip(genres, plays):
        d[g] = d.get(g, 0) + p  # 장르별 재생횟수 딕셔너리에 저장
        
    d = sorted(d.items(), key = (lambda x:x[1]), reverse=True)  # value 값에 따라 내림차순 정렬
    
    for g, p in d:  # 딕셔너리의 key, value 순회
        g_idx = [i for i in range(len(genres)) if g==genres[i]]  # 'g' 장르에 대해서만 index 저장해둠.
        g_play = [plays[p] for p in g_idx]  # g_idx에 해당되는 재생횟수만 저장
        play_list = dict(zip(g_idx, g_play))  # g_idx와 그에 해당하는 재생횟수를 key, value로 저장
        play_list = sorted(play_list.items(), key=(lambda x: x[1]), reverse=True)
        
        answer.append(play_list[0][0])  # 일단 장르당 하나는 무조건 들어감.
        if len(play_list) >= 2:  # 장르당 2개 이상의 노래 있으면, 한 번 더 넣어줌. (최대 2개)
            answer.append(play_list[1][0])
            
    return answer

'''
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

solution(genres, plays)
result : [4, 1, 3, 0]

'''