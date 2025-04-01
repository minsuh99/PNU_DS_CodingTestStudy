# 문제를 푸는 방법이 도저히 안떠올라 블로그와 지피티를 활용해 문제를 리뷰 해보았습니다...

from collections import deque

def bfs(maps, start, end):
    n, m = len(maps), len(maps[0]) # 맵 행렬 크기
    queue = deque([(start[0], start[1], 0)])  # (x좌표, y좌표, 이동 횟수)
    visited = set([start])  # 방문한 위치 저장 중복 방문 방지

    # 상, 하, 좌, 우 이동 방향
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, count = queue.popleft() # 현재 위치와 이동횟수

        # 목적지 도착하면 이동 횟수 반환
        if (x, y) == end:
            return count
        # 4가지 방향으로 이동 가능 여부 확인
        for dx, dy in directions:
            # 다음 이동할 위치 계산
            nx, ny = x + dx, y + dy

            # 범위 안에 있고, 벽이 아니고, 방문하지 않은 곳이면 이동
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X' and (nx, ny) not in visited:
                visited.add((nx, ny)) # 방문 기록 추가
                queue.append((nx, ny, count + 1)) # 큐에 추가하여 탐색 계속 진행

    return -1  # 도착할 수 없으면 -1 반환

def solution(maps):
    # S, L, E 위치 찾기
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':  # 시작점
                start = (i, j)
            elif maps[i][j] == 'L':  # 레버
                lever = (i, j)
            elif maps[i][j] == 'E':  # 출구
                exit = (i, j)

    # S -> L 거리 찾기
    to_lever = bfs(maps, start, lever)
    if to_lever == -1:  # 이동 불가하면 실패
        return -1

    # L -> E 거리 찾기
    to_exit = bfs(maps, lever, exit)
    if to_exit == -1:  # 이동 불가하면 실패
        return -1

    # 총 이동 횟수 반환
    return to_lever + to_exit



'''
테스트 1 〉	통과 (0.04ms, 10.2MB)
테스트 2 〉	통과 (0.20ms, 10.2MB)
테스트 3 〉	통과 (0.16ms, 10.3MB)
테스트 4 〉	통과 (0.11ms, 10.2MB)
테스트 5 〉	통과 (0.29ms, 10.2MB)
테스트 6 〉	통과 (0.18ms, 10.3MB)
테스트 7 〉	통과 (3.60ms, 10.2MB)
테스트 8 〉	통과 (6.21ms, 10.1MB)
테스트 9 〉	통과 (0.05ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.1MB)
테스트 11 〉	통과 (1.33ms, 10.2MB)
테스트 12 〉	통과 (4.71ms, 10.1MB)
테스트 13 〉	통과 (7.51ms, 10.3MB)
테스트 14 〉	통과 (7.38ms, 10.2MB)
테스트 15 〉	통과 (0.48ms, 10.2MB)
테스트 16 〉	통과 (13.46ms, 10.9MB)
테스트 17 〉	통과 (14.99ms, 11MB)
테스트 18 〉	통과 (0.23ms, 10.2MB)
테스트 19 〉	통과 (0.19ms, 10.2MB)
테스트 20 〉	통과 (9.40ms, 10.4MB)
테스트 21 〉	통과 (3.48ms, 10.1MB)
테스트 22 〉	통과 (0.19ms, 10.2MB)
테스트 23 〉	통과 (0.07ms, 10.2MB)


'''