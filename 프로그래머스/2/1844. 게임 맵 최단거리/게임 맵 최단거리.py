def solution(maps):
    from collections import deque
    n = len(maps[0])
    m = len(maps)
    
    # queue 설정
    queue = deque()
    queue.append((0,0,1))
    visited_array = [[False for i in range(n)] for i in range(m)]
    
    # 이동 설정
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y, distance = queue.popleft()
        if x == m-1 and y == n-1:
            return distance
        
        for move_x, move_y in zip(dx, dy):
            if x + move_x < 0 or x+move_x > m-1 or y+move_y < 0 or y+move_y > n-1:
                continue
            if maps[x+move_x][y+move_y] == 1 and not visited_array[x+move_x][y+move_y]:
                visited_array[x+move_x][y+move_y] = True
                queue.append((x+move_x, y+move_y, distance+1))
        
    return -1