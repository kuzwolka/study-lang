def solution(k, tangerine):
    tangdic = dict.fromkeys(tangerine,0)
    for x in tangerine:
        tangdic[x] += 1
    num = sorted(tangdic.values())
    
    answer = 0
    while(k > 0):
        k -= num.pop()
        answer += 1
    return answer