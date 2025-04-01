# 블로그 글 참조, 디버깅하면서 알아가보기
# https://velog.io/@sihoon_cho/Python%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%99%84%EC%A0%84%EC%A0%95%EB%B3%B5-BFS-%EB%84%88%EB%B9%84%EC%9A%B0%EC%84%A0%ED%83%90%EC%83%89


from collections import deque

def BFS(start_x, start_y, end_x, end_y, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n, m = len(graph), len(graph[0])

    # 응용 포인트1: (좌표x, 좌표y, 거리)
    visited = set([(start_x, start_y)])
    queue = deque([(start_x, start_y, 1)])

    while queue:
        x, y, dist = queue.popleft()

        # 응용 포인트2: 문제에서 제시하는 종료 조건
        if x == end_x and y == end_y:
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if (nx, ny) not in visited:
                    # 응용 포인트3: 문제에서 제시하는 추가 이동 조건
                    if graph[nx][ny] == "O":
                        # 응용 포인트1: (다음좌표x, 다음좌표y, 현재거리 + 1)
                        visited.add((nx, ny))
                        queue.append((nx, ny, dist + 1))

    return -1


def solution():
    graph = [
        ['O', 'O', 'O', 'O', 'O', 'X'],
        ['O', 'O', 'O', 'O', 'X', 'O'],
        ['O', 'O', 'O', 'X', 'O', 'O'],
        ['O', 'O', 'X', 'O', 'O', 'O'],
        ['X', 'O', 'O', 'O', 'O', 'O'],
    ]
    
    print(BFS(0, 0, 1, 1, graph))
    

solution()
    
