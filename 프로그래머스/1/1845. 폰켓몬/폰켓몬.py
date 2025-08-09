def solution(nums):
    from collections import Counter
    poke = len(Counter(nums))
    target = int(len(nums)/2)
    
    if poke < target:
        return poke
    else:
        return target
