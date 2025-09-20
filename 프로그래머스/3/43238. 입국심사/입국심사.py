def solution(n, times):
    start = 1
    end = max(times)*n
    answer = 0
    
    while start <= end:
        inspected_people = 0
        mid = (start + end) // 2
        
        for time in times:
            inspected_people += mid // time
            if inspected_people >= n:
                break
                
        if inspected_people >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer