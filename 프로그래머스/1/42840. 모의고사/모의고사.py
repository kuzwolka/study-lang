def solution(answers):
    first_su = [1,2,3,4,5]
    second_su = [2, 1, 2, 3, 2, 4, 2, 5]
    third_su = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    def scoring(answers, su):
        score = 0
        s = len(su)
        cnt = len(answers)//s
        if len(answers)%s != 0:
            cnt += 1
            
        for i in range(cnt):
            index = (i+1)*s
            if index > len(answers):
                index = len(answers)
            for res, ans in zip(su, answers[i*s:index]):
                if res == ans:
                    score += 1
        return score
    
    final = [scoring(answers, first_su), scoring(answers, second_su), scoring(answers, third_su)]
    max_score = max(final)
    return [(x+1) for x,y in enumerate(final) if y == max_score]
    
    
    