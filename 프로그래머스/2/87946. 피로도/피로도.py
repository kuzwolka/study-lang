def solution(k, dungeons):
    from itertools import permutations
    p = list(permutations(dungeons))
    
    def dungeon_expedition(k: int, dungeon_route: list):
        num_of_dungeon = 0
        for exhaust_condition, exhaust_deduction in dungeon_route:
            if k < exhaust_condition:
                continue
            k -= exhaust_deduction
            num_of_dungeon += 1
        return num_of_dungeon
    
    num_of_dungeon_list = []
    for dungeon_route in p:
        num_of_dungeon_list.append(dungeon_expedition(k, dungeon_route))

    return max(num_of_dungeon_list)
    