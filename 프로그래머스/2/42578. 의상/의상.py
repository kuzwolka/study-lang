def solution(clothes):
    kind = dict.fromkeys(set([i[1] for i in clothes]), 0)
    
    for cloth in clothes:
        kind[cloth[1]] += 1

    answer = 1
    for i in kind.values():
        answer *= (i+1)
    return answer-1
        
        
