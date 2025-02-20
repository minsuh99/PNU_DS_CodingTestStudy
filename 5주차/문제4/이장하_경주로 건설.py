from collections import deque


def solution(board): 
    N = len(board)

    # 최소 건설 비용 초기화
    answer = float("inf")

    # 어느 방향에서 왔는지 알아야 하므로 인덱스까지 정의
    delta = [(-1,0,0), (0,-1,1), (1,0,2), (0,1,3)]
    
    # 이전 방향별로 최소 비용 계산
    costs = [[[float("inf")] * N for _ in range(N)] for _ in range(4)]
    
    # 시작 지점 비용 초기화
    for i in range(4):
        costs[i][0][0] = 0
    
    # 시작 지점은 이전 방향이 없으므로 -1
    queue = deque([(-1, 0, 0, 0)])
    
    while queue:
        i, x, y, cost = queue.popleft()
        
        # 도착점에 도착했을 때 적은 비용으로 업데이트
        if x == N-1 and y == N-1 and answer > cost:
            answer = cost
        
        for dx, dy, dir_ in delta:
            nx , ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                # 이전 방향과 진행 방향이 같거나 시작점에서 온 경우 직선도로 
                if i == dir_ or i == -1:
                    n_cost = 100
                # 방향이 달라지는 경우 코너
                else: n_cost = 600
                
                # 이동한 지점까지 건설 비용이 적어지면 업데이트
                if costs[dir_][nx][ny] > cost + n_cost:
                    costs[dir_][nx][ny] = cost + n_cost

                    # 비용이 적게 건설된 지점부터 다시 이동
                    queue.append((dir_, nx, ny, cost + n_cost))

    return answer


'''
정확성  테스트
테스트 1 〉    통과 (0.05ms, 10.3MB)
테스트 2 〉    통과 (0.03ms, 10.1MB)
테스트 3 〉    통과 (0.03ms, 10.3MB)
테스트 4 〉    통과 (0.07ms, 10.2MB)
테스트 5 〉    통과 (0.08ms, 10.2MB)
테스트 6 〉    통과 (0.57ms, 10.2MB)
테스트 7 〉    통과 (0.68ms, 10.3MB)
테스트 8 〉    통과 (0.53ms, 10.3MB)
테스트 9 〉    통과 (1.37ms, 10.4MB)
테스트 10 〉    통과 (1.09ms, 10.4MB)
테스트 11 〉    통과 (28.83ms, 10.2MB)
테스트 12 〉    통과 (4.57ms, 10.4MB)
테스트 13 〉    통과 (0.34ms, 10.4MB)
테스트 14 〉    통과 (0.48ms, 10.4MB)
테스트 15 〉    통과 (2.09ms, 10.4MB)
테스트 16 〉    통과 (4.36ms, 10.1MB)
테스트 17 〉    통과 (11.23ms, 10.2MB)
테스트 18 〉    통과 (6.25ms, 10.3MB)
테스트 19 〉    통과 (16.60ms, 10.4MB)
테스트 20 〉    통과 (1.89ms, 10.3MB)
테스트 21 〉    통과 (1.22ms, 10.4MB)
테스트 22 〉    통과 (0.22ms, 10.3MB)
테스트 23 〉    통과 (0.10ms, 10.4MB)
테스트 24 〉    통과 (0.11ms, 10.2MB)
테스트 25 〉    통과 (0.07ms, 10.4MB)
'''
