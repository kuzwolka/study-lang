def solution(scoville, K):
    import heapq
    heapq.heapify(scoville)
    iteration = 0
    
    while(len(scoville) >= 2):
        min_ = heapq.heappop(scoville)
        if min_ >= K:
            return iteration
        else:
            next_min = heapq.heappop(scoville)
            heapq.heappush(scoville, min_ + (next_min*2))
            iteration += 1
    if scoville[0] >= K:
        return iteration
    return -1
            