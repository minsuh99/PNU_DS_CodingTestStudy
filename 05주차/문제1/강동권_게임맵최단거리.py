from collections import deque

directions = [(1,0),(-1,0),(0,1),(0,-1)]

def solution(maps):
    m = len(maps)   
    n = len(maps[0]) 
    visited = [[0] * n for _ in range(m)]
    
    queue = deque()
    queue.append([0, 0, 1])  

    while queue:
        curx, cury, count = queue.popleft()
        
        if curx == m - 1 and cury == n - 1:
            return count

        for dir in directions:
            new_x, new_y = curx + dir[0], cury + dir[1]

            if 0 <= new_x < m and 0 <= new_y < n:  
                if visited[new_x][new_y] == 0 and maps[new_x][new_y] == 1:
                    queue.append([new_x, new_y, count + 1])
                    visited[new_x][new_y] = 1  

    return -1

# 정확성  테스트
# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (0.04ms, 10.4MB)
# 테스트 4 〉	통과 (0.03ms, 10.4MB)
# 테스트 5 〉	통과 (0.03ms, 10.4MB)
# 테스트 6 〉	통과 (0.04ms, 10.2MB)
# 테스트 7 〉	통과 (0.07ms, 10.2MB)
# 테스트 8 〉	통과 (0.04ms, 10.3MB)
# 테스트 9 〉	통과 (0.06ms, 10.2MB)
# 테스트 10 〉	통과 (0.05ms, 10.2MB)
# 테스트 11 〉	통과 (0.03ms, 10.3MB)
# 테스트 12 〉	통과 (0.03ms, 10.2MB)
# 테스트 13 〉	통과 (0.03ms, 10.2MB)
# 테스트 14 〉	통과 (0.03ms, 10.4MB)
# 테스트 15 〉	통과 (0.03ms, 10.3MB)
# 테스트 16 〉	통과 (0.02ms, 10.2MB)
# 테스트 17 〉	통과 (0.05ms, 10.4MB)
# 테스트 18 〉	통과 (0.01ms, 10.3MB)
# 테스트 19 〉	통과 (0.01ms, 10.3MB)
# 테스트 20 〉	통과 (0.01ms, 10.2MB)
# 테스트 21 〉	통과 (0.01ms, 10.2MB)
# 효율성  테스트
# 테스트 1 〉	통과 (10.65ms, 10.2MB)
# 테스트 2 〉	통과 (3.09ms, 10.4MB)
# 테스트 3 〉	통과 (7.73ms, 10.3MB)
# 테스트 4 〉	통과 (4.78ms, 10.3MB)
