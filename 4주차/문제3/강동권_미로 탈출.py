from collections import deque

moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def solution(maps):
    MAX_Y = len(maps) - 1  # Rows
    MAX_X = len(maps[0]) - 1  # Columns
    
    queue = deque()
    visited = set()  # Store (x, y, lever_state) 

    # Find 'S'
    for i in range(MAX_Y + 1):
        for j in range(MAX_X + 1):
            if maps[i][j] == 'S':
                start_x, start_y = i, j
                break
    
    queue.append((start_x, start_y, 0, 0))  # (x, y, move_count, lever_state)
    visited.add((start_x, start_y, 0)) 

    while queue:
        cur_x, cur_y, count, lever = queue.popleft()
        
        for dx, dy in moves:
            nx, ny = cur_x + dx, cur_y + dy

            if 0 <= nx <= MAX_Y and 0 <= ny <= MAX_X:
                cell = maps[nx][ny]
                
                if cell == 'X':  
                    continue
                
                new_lever = lever or (cell == 'L')

                if cell == 'E' and new_lever:
                    return count + 1 
                
                if (nx, ny, new_lever) not in visited:
                    visited.add((nx, ny, new_lever))
                    queue.append((nx, ny, count + 1, new_lever))

    return -1 

# 테스트 1 〉	통과 (0.06ms, 10.4MB)
# 테스트 2 〉	통과 (0.10ms, 10.4MB)
# 테스트 3 〉	통과 (0.21ms, 10.3MB)
# 테스트 4 〉	통과 (0.19ms, 10.3MB)
# 테스트 5 〉	통과 (0.15ms, 10.3MB)
# 테스트 6 〉	통과 (0.09ms, 10.4MB)
# 테스트 7 〉	통과 (2.34ms, 10.4MB)
# 테스트 8 〉	통과 (3.62ms, 10.4MB)
# 테스트 9 〉	통과 (0.04ms, 10.2MB)
# 테스트 10 〉	통과 (0.02ms, 10.4MB)
# 테스트 11 〉	통과 (2.09ms, 10.4MB)
# 테스트 12 〉	통과 (7.56ms, 11MB)
# 테스트 13 〉	통과 (6.24ms, 10.5MB)
# 테스트 14 〉	통과 (13.44ms, 10.6MB)
# 테스트 15 〉	통과 (0.44ms, 10.2MB)
# 테스트 16 〉	통과 (13.03ms, 11MB)
# 테스트 17 〉	통과 (19.43ms, 11.3MB)
# 테스트 18 〉	통과 (0.19ms, 10.4MB)
# 테스트 19 〉	통과 (0.19ms, 10.3MB)
# 테스트 20 〉	통과 (11.85ms, 11MB)
# 테스트 21 〉	통과 (2.20ms, 10.4MB)
# 테스트 22 〉	통과 (0.15ms, 10.3MB)
# 테스트 23 〉	통과 (0.04ms, 10.3MB)
