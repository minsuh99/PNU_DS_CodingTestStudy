from collections import deque



def bfs(start_x, start_y, end_x, end_y, maps): # 최단거리 문제 -> bfs
    row = len(maps)
    col = len(maps[0])
    dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우
    visited = set([(start_x, start_y)]) # 탐색했던 지점 담을 set
    queue = deque([(start_x, start_y, 0)]) # (x, y, 거리)로 설정
    
    
    while queue:
        x, y, dist = queue.popleft()
        
        if x == end_x and y == end_y: # 원하는 지점까지 왔으면
            return dist # 움직인 거리 return
        
        for d in dxdy:
            x_, y_ = x + d[0], y + d[1]
            
            if 0 <= x_ < row and 0 <= y_ < col:
                if (x_, y_) not in visited:
                    if maps[x_][y_] in ["S", "L", "O", "E"]: # 이동 가능한 경우에
                        visited.add((x_, y_)) # 방문한 노드 추가 (set이라서 이미 존재하는 경우 add가 안됨)
                        queue.append((x_, y_, dist+1)) # 다음 방문할 노드이니까 queue에 append
    
    return -1

def solution(maps):
    for x in range(len(maps)): # 시작점 S, 레버 L, 탈출구 E 좌표 정보 얻을 반복문 (최대 10,000번)
        for y in range(len(maps[0])):
            if maps[x][y] == "S":
                sx, sy = x, y
            elif maps[x][y] == "L":
                lx, ly = x, y
            elif maps[x][y] == "E":
                ex, ey = x, y
    
    dist1 = bfs(sx, sy, lx, ly, maps) # 시작점 -> 레버
    dist2 = bfs(lx, ly, ex, ey, maps) # 레버 -> 탈출구
    
    if dist1 != -1 and dist2 != -1: # 둘 중 하나라도 방문 못 하는 경우가 생기면 -1 리턴
        return dist1 + dist2
    else:
        return -1
    

'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.13ms, 10.2MB)
테스트 3 〉	통과 (0.16ms, 10.3MB)
테스트 4 〉	통과 (0.13ms, 10.2MB)
테스트 5 〉	통과 (0.19ms, 10.2MB)
테스트 6 〉	통과 (0.10ms, 10.2MB)
테스트 7 〉	통과 (2.17ms, 10.4MB)
테스트 8 〉	통과 (3.49ms, 10.2MB)
테스트 9 〉	통과 (0.06ms, 10.2MB)
테스트 10 〉	통과 (0.03ms, 10.2MB)
테스트 11 〉	통과 (0.75ms, 10.2MB)
테스트 12 〉	통과 (5.58ms, 10.3MB)
테스트 13 〉	통과 (6.01ms, 10.3MB)
테스트 14 〉	통과 (5.18ms, 10.4MB)
테스트 15 〉	통과 (0.50ms, 10.2MB)
테스트 16 〉	통과 (12.70ms, 10.9MB)
테스트 17 〉	통과 (15.11ms, 11MB)
테스트 18 〉	통과 (0.28ms, 10.2MB)
테스트 19 〉	통과 (0.20ms, 10.3MB)
테스트 20 〉	통과 (9.43ms, 10.5MB)
테스트 21 〉	통과 (2.13ms, 10.3MB)
테스트 22 〉	통과 (0.19ms, 10.2MB)
테스트 23 〉	통과 (0.05ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''