def solution(numbers, target):
    stack = [(0,0)]
    answer = 0
    
    while(stack):
        indx, num = stack.pop()
        
        if indx == len(numbers):
            if num == target:
                answer+=1
            continue
        
        stack.append((indx +1, num + numbers[indx]))
        stack.append((indx +1, num - numbers[indx]))
    return answer