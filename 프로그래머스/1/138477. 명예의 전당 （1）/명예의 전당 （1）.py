def solution(k, score):
    score = score[::-1]
    window = []
    answer = []
    
    while(score):
        window.append(score.pop())
        leng = len(window)
        window.sort()
        
        if leng < k:
            answer.append(window[0])
        else:
            answer.append(window[leng-k])
            
    return answer