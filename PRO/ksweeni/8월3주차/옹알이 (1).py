def solution(babbling):
    can = ['aya','ye','woo','ma'];
    answer = 0
    for i in range(len(babbling)):
        for c in can:
            if (c in babbling[i]) and (c*2 not in babbling[i]):
                babbling[i] = babbling[i].replace(c,"-")
        if all(b == "-" for b in babbling[i]):
            answer+=1
    return answer