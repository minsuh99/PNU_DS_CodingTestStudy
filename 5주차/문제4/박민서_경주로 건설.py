# BFS를 이용, 최저 cost를 구하려 함
# 처음 84점이 나온 이후 gpt에 도움을 얻음
# 같은 점에 도달했을 때에 최저 cost만 저장하게하는 cost 딕셔너리 생성하자는 답을 얻음

from collections import defaultdict, deque

def bfs(start_x, start_y, maps):
    n = len(maps)
    res = []
    dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # visited = set([(start_x, start_y)]) 기존 코드 (방문만 신경쓴,,)
    queue = deque([(start_x, start_y, "", 0)])
    cost = defaultdict(lambda :float("inf")) # 수정 코드
    cost[(0, 0, '')] = 0
    

    while queue:
        queue = deque(sorted(queue, key=lambda x:x[3]))
        x, y, direction, dist = queue.popleft()
        
        if cost[(x, y, direction)] and dist > cost[(x, y, direction)]: # 수정 코드 (최저만 신경씀)
            continue
        
        if x == n - 1 and y == n - 1:
            res.append(dist)
            
        for d in dxdy:
            if d in [(-1, 0), (1, 0)]: # 들어온 방향 신경써야함
                new_dir = "ver"
            else:
                new_dir = "hor"
            x_, y_ = x + d[0], y + d[1]
            if 0 <= x_ < n and 0 <= y_ < n and maps[x_][y_] == 0:
                if direction == "" or direction == new_dir:
                    dist_ =  dist + 1
                else:
                    dist_ = dist + 6 # dist + 1(도로 건설) + 5(코너)
            
                if dist_ < cost[(x_, y_, new_dir)]: # 수정 코드 (같은 점에 최저 cost가 아니면 queue에 추가하지 않음음)
                    cost[(x_, y_, new_dir)] = dist_
                    queue.append((x_, y_, new_dir, dist_))
    return res

def solution(board):
    answer = min(bfs(0, 0, board)) * 100
    return answer


'''
정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.4MB)
테스트 3 〉	통과 (0.04ms, 10.2MB)
테스트 4 〉	통과 (0.13ms, 10.2MB)
테스트 5 〉	통과 (0.16ms, 10.3MB)
테스트 6 〉	통과 (0.66ms, 10.3MB)
테스트 7 〉	통과 (0.69ms, 10.2MB)
테스트 8 〉	통과 (0.68ms, 10.2MB)
테스트 9 〉	통과 (0.71ms, 10.2MB)
테스트 10 〉	통과 (1.37ms, 10.2MB)
테스트 11 〉	통과 (4.57ms, 10.3MB)
테스트 12 〉	통과 (21.51ms, 10.1MB)
테스트 13 〉	통과 (0.28ms, 10.1MB)
테스트 14 〉	통과 (0.40ms, 10.4MB)
테스트 15 〉	통과 (1.64ms, 10.3MB)
테스트 16 〉	통과 (4.44ms, 10.2MB)
테스트 17 〉	통과 (3.52ms, 10.2MB)
테스트 18 〉	통과 (6.34ms, 10.4MB)
테스트 19 〉	통과 (4.15ms, 10.4MB)
테스트 20 〉	통과 (1.68ms, 10.1MB)
테스트 21 〉	통과 (2.09ms, 10.4MB)
테스트 22 〉	통과 (0.14ms, 10.4MB)
테스트 23 〉	통과 (0.12ms, 10.4MB)
테스트 24 〉	통과 (0.13ms, 10MB)
테스트 25 〉	통과 (0.09ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''