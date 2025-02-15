from collections import deque
# 혼자 짜보기 (bfs 이용 최단거리 찾기)
# def bfs(start_x, start_y, end_x, end_y, maps): 
# 기존에 이렇게 짰는데, [목표지점] end_x, end_y가 maps의 오른쪽 하단점으로 고정이라 없어도 될 듯
def bfs(start_x, start_y, maps):
    n = len(maps)
    m = len(maps[0])
    dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set([(start_x, start_y)])
    queue = deque([(start_x, start_y, 1)])
    
    while queue:
        x, y, dist = queue.popleft()
        if x == n -1 and y == m - 1:
            return dist
        for d in dxdy:
            x_, y_ = x + d[0], y + d[1]
            if 0 <= x_ < n and 0 <= y_ < m:
                if (x_, y_) not in visited:
                    if maps[x_][y_] == 1:
                        visited.add((x_, y_))
                        queue.append((x_, y_, dist + 1))
    return -1
    
    

def solution(maps):
    answer = bfs(0, 0, maps)
    return answer


'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.06ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.1MB)
테스트 7 〉	통과 (0.06ms, 10.2MB)
테스트 8 〉	통과 (0.05ms, 10.2MB)
테스트 9 〉	통과 (0.08ms, 10.2MB)
테스트 10 〉	통과 (0.09ms, 10.1MB)
테스트 11 〉	통과 (0.03ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.3MB)
테스트 13 〉	통과 (0.03ms, 10.4MB)
테스트 14 〉	통과 (0.03ms, 10.3MB)
테스트 15 〉	통과 (0.03ms, 10.3MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
테스트 17 〉	통과 (0.04ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.3MB)
테스트 19 〉	통과 (0.01ms, 10.2MB)
테스트 20 〉	통과 (0.01ms, 10.4MB)
테스트 21 〉	통과 (0.01ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (12.24ms, 11.1MB)
테스트 2 〉	통과 (3.38ms, 10.5MB)
테스트 3 〉	통과 (8.70ms, 10.9MB)
테스트 4 〉	통과 (5.07ms, 10.3MB)
채점 결과
정확성: 69.9
효율성: 30.1
합계: 100.0 / 100.0
'''