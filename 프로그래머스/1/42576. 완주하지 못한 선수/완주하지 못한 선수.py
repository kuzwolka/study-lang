def solution(participant, completion):
    from collections import Counter
    participant_dict = Counter(participant)
    for x in completion:
        participant_dict[x] -= 1
    for name, numb in participant_dict.items():
        if numb != 0:
            return name    

# Collections 없이 -> 실패
# part = dict.fromkeys(participant)
#     part = {x: participant.count(x) for x in set(participant)}
    
#     for x in completion:
#         part[x] -= 1
    
#     for name, num in part.items():
#         if num != 0:
#             return name
