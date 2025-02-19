from collections import deque

# 너비 우선 탐색으로 최단거리 탐색
def bfs(start, maps, n, m):
    delta = [(0,1), (0,-1), (1,0), (-1,0)]
    queue = deque([start])
    # 방문한 칸을 체크할 2차원 리스트
    visited = [[0] * m for _ in range(n)]
    # 시작점 방문표시
    visited[start[0]][start[1]] = 1
    
    # 다음 방문할 칸이 없어질때 까지
    while queue:
        x, y = queue.popleft()
        # 적 팀의 진영에 도착하면 최단거리 반환
        if (x,y) == (n-1,m-1):
            return visited[x][y]
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            # 다음 이동할 칸이 맵 안이고 벽이 아니고 방문한 적이 없을 경우 이동
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                # 이동 전 칸까지의 이동거리 + 1
                visited[nx][ny] = visited[x][y] + 1
                # 이동 후 다음 칸으로 또 이동해야 함
                queue.append((nx,ny))
    # 적 팀의 진영에 도착하지 못할 경우 -1 반환
    return -1


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = bfs((0,0), maps, n, m)
    return answer


'''
정확성  테스트
테스트 1 〉    통과 (0.03ms, 10.3MB)
테스트 2 〉    통과 (0.02ms, 10.3MB)
테스트 3 〉    통과 (0.04ms, 10.3MB)
테스트 4 〉    통과 (0.07ms, 10.2MB)
테스트 5 〉    통과 (0.03ms, 10.2MB)
테스트 6 〉    통과 (0.04ms, 10.3MB)
테스트 7 〉    통과 (0.07ms, 10.3MB)
테스트 8 〉    통과 (0.05ms, 10.2MB)
테스트 9 〉    통과 (0.06ms, 10.3MB)
테스트 10 〉    통과 (0.05ms, 10.2MB)
테스트 11 〉    통과 (0.06ms, 10.3MB)
테스트 12 〉    통과 (0.04ms, 10.2MB)
테스트 13 〉    통과 (0.04ms, 10.1MB)
테스트 14 〉    통과 (0.04ms, 10.1MB)
테스트 15 〉    통과 (0.05ms, 10.4MB)
테스트 16 〉    통과 (0.03ms, 10.2MB)
테스트 17 〉    통과 (0.08ms, 10.2MB)
테스트 18 〉    통과 (0.01ms, 10.3MB)
테스트 19 〉    통과 (0.01ms, 10.2MB)
테스트 20 〉    통과 (0.01ms, 10.2MB)
테스트 21 〉    통과 (0.01ms, 10.3MB)
효율성  테스트
테스트 1 〉    통과 (11.63ms, 10.5MB)
테스트 2 〉    통과 (3.15ms, 10.3MB)
테스트 3 〉    통과 (7.25ms, 10.3MB)
테스트 4 〉    통과 (4.58ms, 10.3MB)
'''
