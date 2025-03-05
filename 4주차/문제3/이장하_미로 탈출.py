from collections import deque

# 너비 우선 탐색으로 최단거리 찾기
def bfs(start, maps, row, col):
    delta = [(-1,0), (1,0), (0,-1), (0,1)]
    queue = deque([start])
    # 방문한 칸을 체크할 2차원 리스트
    visited = [[0]*col for _ in range(row)]
    # 시작점 방문표시
    visited[start[0]][start[1]] = 1
    
    # 다음 방문할 칸이 없어질때 까지
    while queue:
        x, y = queue.popleft()
        # 레버에 도착하면 이동한 최단거리 반환
        if maps[x][y] == "L":
            # 시작을 1로 했으므로 1을 빼줌
            return visited[x][y] -1
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            # 다음 이동할 칸이 미로안이고, 벽이 아니고, 방문한 적이 없는 경우에만 이동
            if 0 <= nx < row and 0 <= ny < col and maps[nx][ny] != "X" and visited[nx][ny] == 0:
                # 이동한 칸은 전 칸까지 이동한 거리 + 1
                visited[nx][ny] = visited[x][y] + 1
                # 이동한 칸에서 또 이동을 해야하므로 큐에 넣음
                queue.append((nx,ny))
    return False
    

def solution(maps):
    answer = 0
    row = len(maps)
    col = len(maps[0])
    for x in range(row):
        for y in range(col):
            # 문제에서 레버를 당기러 갈때 출구를 지날 수 있으므로, 출구에 처음 도착이 종료 조건이 아님
            # 시작부터 레버까지 최단거리 + 출구에서 레버까지 최단거리가 정답
            if maps[x][y] in ["S", "E"]:
                '''
                레버까지 갈 수 있는지 없는지 확인하는 플래그
                그냥 answer==0 으로 확인할 경우, 시작부터 레버까지는 갈 수 있지만 
                도착에서 못 가는 경우를 예외처리 하지 못함
                '''
                flag = answer
                answer += bfs((x,y), maps, row, col)
                # 레버까지 갈 수 없으면 False를 반환하여 정답의 변화가 없으므로 -1 반환
                if answer == flag:
                    return -1

    return answer


'''
정확성  테스트
테스트 1 〉    통과 (0.03ms, 10.3MB)
테스트 2 〉    통과 (0.11ms, 10.1MB)
테스트 3 〉    통과 (0.17ms, 10.3MB)
테스트 4 〉    통과 (0.09ms, 10.2MB)
테스트 5 〉    통과 (0.15ms, 10.2MB)
테스트 6 〉    통과 (0.11ms, 10.3MB)
테스트 7 〉    통과 (1.68ms, 10.1MB)
테스트 8 〉    통과 (2.89ms, 10.4MB)
테스트 9 〉    통과 (0.04ms, 10.3MB)
테스트 10 〉    통과 (0.02ms, 10.4MB)
테스트 11 〉    통과 (0.34ms, 10.2MB)
테스트 12 〉    통과 (3.57ms, 10.2MB)
테스트 13 〉    통과 (5.79ms, 10.2MB)
테스트 14 〉    통과 (3.36ms, 10.2MB)
테스트 15 〉    통과 (0.44ms, 10.1MB)
테스트 16 〉    통과 (8.01ms, 10.4MB)
테스트 17 〉    통과 (8.99ms, 10.3MB)
테스트 18 〉    통과 (0.15ms, 10.3MB)
테스트 19 〉    통과 (0.18ms, 10.4MB)
테스트 20 〉    통과 (3.57ms, 10.2MB)
테스트 21 〉    통과 (1.73ms, 10.3MB)
테스트 22 〉    통과 (0.14ms, 10.4MB)
테스트 23 〉    통과 (0.04ms, 10.3MB)
'''

