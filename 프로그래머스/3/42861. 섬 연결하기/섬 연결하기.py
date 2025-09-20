def solution(n, costs):
    answer = 0
    # 탐욕적 선택을 위한 costs sort(비용 기준)
    for cost in costs:
        cost[0:2].sort()
    costs.sort(key = lambda x: x[2])
    
    island_group = [i for i in range(n)]
    def island_connection_check(island_group: list):
        if len(set(island_group)) == 1:
            return True
        return False
    
    iteration = 0
    while not island_connection_check(island_group):
        if len(costs[iteration]) == 3:
            a_island, b_island, cost = costs[iteration]
            if island_group[a_island] != island_group[b_island]:
                answer += cost
                temp = island_group[b_island]
                for i in range(n):
                    if island_group[i] == temp:
                        island_group[i] = island_group[a_island]
            
        iteration += 1
    
    return answer
        