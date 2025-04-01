from collections import deque


def solution(land, height):
    global answer
    answer = 0
    N = len(land)
    
    # 사다리 없이 이동할 수 있는 칸들을 같은 색깔로 묶을 맵
    MAP = [[0] * N for _ in range(N)]
    delta = [(0,1), (1,0), (0,-1), (-1,0)]
    # bfs로 사다리 없이 갈 수 있으면 같은 색으로 정의
    color = 1
    for i in range(N):
        for j in range(N):
            if not MAP[i][j]:
                queue = deque([(i,j)])
                MAP[i][j] = color
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in delta:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and not MAP[nx][ny] and abs(land[nx][ny] - land[x][y]) <= height:
                            MAP[nx][ny] = color
                            queue.append((nx, ny)) 
                color += 1
    
    # 사다리
    ladders = []
    for x in range(N):
        for y in range(N):
            # 오른쪽이랑 아래로만 연결할 수 있는지 확인하면 중복을 없앨 수 있음
            for dx, dy in delta[:2]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and MAP[nx][ny] != MAP[x][y]:
                    ladders.append((abs(land[nx][ny] - land[x][y]), (x,y), (nx,ny)))
    # 최소 비용인 사다리부터 설치
    ladders.sort(key = lambda x : x[0])
    
    # 유니온 파인드
    parent = [x for x in range(color+1)]
    
    def find(x):
        if parent[x] != x:
            return find(parent[x])
        return x
    
    def union(a, b, cost):
        global answer
        a = find(a)
        b = find(b)
        # 부모가 다른경우 사다리를 설치하고 비용추가, 부모 업데이트
        if a != b:
            answer += cost
            if a < b:
                parent[b] = a
            else:
                parent[a] = b
    
    for cost, (x1, y1), (x2, y2) in ladders:
        a = MAP[x1][y1]
        b = MAP[x2][y2]
        union(a, b, cost)
            
    return answer

'''
정확성  테스트
테스트 1 〉    통과 (0.08ms, 9.21MB)
테스트 2 〉    통과 (0.08ms, 9.29MB)
테스트 3 〉    통과 (0.10ms, 9.18MB)
테스트 4 〉    통과 (0.11ms, 9.09MB)
테스트 5 〉    통과 (0.11ms, 9.2MB)
테스트 6 〉    통과 (0.11ms, 9.02MB)
테스트 7 〉    통과 (0.08ms, 9.15MB)
테스트 8 〉    통과 (0.11ms, 9.25MB)
테스트 9 〉    통과 (0.10ms, 9.11MB)
테스트 10 〉    통과 (0.10ms, 9.14MB)
테스트 11 〉    통과 (0.09ms, 9.29MB)
테스트 12 〉    통과 (0.13ms, 8.99MB)
테스트 13 〉    통과 (0.09ms, 9.32MB)
테스트 14 〉    통과 (0.24ms, 9.05MB)
테스트 15 〉    통과 (1.84ms, 9.24MB)
테스트 16 〉    통과 (12.81ms, 10.1MB)
테스트 17 〉    통과 (53.94ms, 13.3MB)
테스트 18 〉    통과 (60.90ms, 13MB)
테스트 19 〉    통과 (46.32ms, 12.6MB)
테스트 20 〉    통과 (309.14ms, 28.2MB)
테스트 21 〉    통과 (325.78ms, 28.9MB)
테스트 22 〉    통과 (778.13ms, 50.4MB)
테스트 23 〉    통과 (656.58ms, 52.4MB)
테스트 24 〉    통과 (146.62ms, 12.9MB)
테스트 25 〉    통과 (169.94ms, 14.2MB)
테스트 26 〉    통과 (757.08ms, 49.8MB)
테스트 27 〉    통과 (730.27ms, 49.7MB)
테스트 28 〉    통과 (719.92ms, 48.8MB)
테스트 29 〉    통과 (660.13ms, 47.4MB)
테스트 30 〉    통과 (707.76ms, 50.7MB)
'''
