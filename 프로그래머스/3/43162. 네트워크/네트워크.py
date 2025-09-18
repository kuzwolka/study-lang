def solution(n, computers):
    from collections import deque
    network = 0
    checked_computer_array = [False for i in range(n)]
    
    for i in range(n):
        # 새로운 네트워크를 찾음
        if not checked_computer_array[i]:
            checked_computer_array[i] = True
            network += 1
            
            # BFS(탐색) 시작
            # 시작점 = 해당 컴퓨터
            queue = deque()
            queue.append(i)
            while queue:
                current_computer = queue.popleft()
                for k in range(n):
                    if computers[current_computer][k] == 1 and not checked_computer_array[k]:
                        checked_computer_array[k] = True
                        queue.append(k)
                    
    return network