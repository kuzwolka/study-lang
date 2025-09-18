def solution(begin, target, words):
    from collections import deque
    def word_distance(start: str, target: str):
        distance = 0
        for b,t in zip(start, target):
            if b != t:
                distance += 1
        return distance
    
    queue = deque()
    queue.append((begin, 0))
    checked_arr = [False for i in range(len(words))]
    
    while queue:
        start_word, distance = queue.popleft()
        if start_word == target:
            return distance
        for i in range(len(words)):
            if word_distance(start_word, words[i]) == 1 and not checked_arr[i]:
                queue.append((words[i], distance+1))
                checked_arr[i] = True
                
    return 0